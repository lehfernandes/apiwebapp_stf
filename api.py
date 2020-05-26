from flask import Flask, request
import pre_process.pre_processamento as pp
import os
app = Flask(__name__)


@app.route('/stf', methods=['POST'])
def quebrarCaptcha():
    #try:
        data = request.get_json()
        img = pp.quebrar_captcha(data["captcha"])
        if img is not None:
            return {"captcha": pp.previsao(img)}, 200
        else:
            return {"captcha": "AAAA"}, 200
    #except:
        #return {
                   #"captcha": "Não foi possível completar a requisição, verifique se o parâmetro captcha foi informado e o base64 é válido"}, 409


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, port=port, host='0.0.0.0')

