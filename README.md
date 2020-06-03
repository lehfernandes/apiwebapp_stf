# apiwebapp_stf

O objetivo deste projeto é criar uma api que consiga realizar uma previsão do texto de uma imagem e entregar no padrão json a resposta para o usuário.

A api recebe uma chamada post com um body json no formato com um parametro captcha e um base64 válido:
  
  {
    "captcha": "base64"
  }
  
Entregando uma resposta no formato:

  {
    "captcha": "previsão"
  }

