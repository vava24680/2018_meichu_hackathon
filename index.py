import json
from flask import Flask, jsonify, make_response, request
from OpenSSL import SSL
import requests
import DAN.DAN as DAN
import parse as parse
import time

cert_path = '/etc/letsencrypt/live/meichu.haohao.in/'
app = Flask(__name__)
context = (cert_path + 'fullchain.pem', cert_path + 'privkey.pem')
DAN.register_on_IoTtalk();

@app.route('/', methods=['POST'])
def webhook():
  print json.dumps(request.get_json(), indent = 2)
  with open('output.txt', 'w+') as f:
    f.write(json.dumps(request.get_json()))
    response = parse.parse(request.get_json())
    if response == 1:
      return jsonify({})
    print response
  return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='446', debug = True, ssl_context = context)
