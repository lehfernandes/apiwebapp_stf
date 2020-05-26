import base64
import numpy as np
import cv2
from keras.models import load_model
import os
import pickle


def cortar_imagem(img):
    try:
        arrayimg = []
        cont = 0
        nparr = np.fromstring(base64.decodebytes(img.encode()), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        for cont in range(4):
            y = 0
            x = 20 * cont
            h = 40
            w = 20
            crop = image[y:y + h, x:x + w]
            lower = np.array([0, 180, 0])
            upper = np.array([100, 180, 100])
            mask = cv2.inRange(crop, lower, upper)
            res = cv2.bitwise_and(crop, crop, mask=mask)
            res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            res = cv2.threshold(res, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
            arrayimg.append(res)
        return arrayimg
    except:
        return None


def quebrar_captcha(base64):
    img = cortar_imagem(base64)
    if img is not None:
        return img
    else:
        return None


def previsao(img):
    captcha = ''
    global model
    model = load_model('model/captcha_model.hdf5')
    model._make_predict_function()
    with open('model/model_labels.dat', "rb") as f:
        lb = pickle.load(f)
    if img is not None:
        for imgP in img:
            imgP = np.stack((imgP,) * 3, axis=-1)
            imgP = cv2.resize(imgP, (50, 50))
            imgP = imgP.reshape(-1, 50, 50, 3)
            prediction = model.predict(imgP)
            captcha = captcha + lb.classes_[np.argmax(prediction)][0]
    return captcha
