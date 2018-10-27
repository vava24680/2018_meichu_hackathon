import json
from flask import Flask, jsonify, make_response, request
from OpenSSL import SSL
import requests
import DAN.DAN as DAN
import time

cert_path = '/etc/letsencrypt/live/meichu.haohao.in/'
app = Flask(__name__)
context = (cert_path + 'fullchain.pem', cert_path + 'privkey.pem')

@app.route('/', methods=['POST'])
def webhook():
  print json.dumps(request.get_json(), indent = 2)
  with open('output.txt', 'w+') as f:
    f.write(json.dumps(request.get_json()))
  return jsonify({"status": "ok"})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='446', debug = True, ssl_context = context)
