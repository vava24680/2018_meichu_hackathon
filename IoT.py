# -*- coding: UTF-8 -*-
import requests
import json

def temperature( device_id ):
    url = 'https://iot.cht.com.tw/iot/v1/device/'
    headers = {'CK': 'PK00GYFN2FDVN032VX'}
    response = requests.get(url, headers=headers)
    device = json.loads(response.text)

    d_item = device[device_id]
    url = 'https://iot.cht.com.tw/iot/v1/device/'+str(d_item['id'])+'/sensor'
    response = requests.get(url, headers=headers)
    sensor = json.loads(response.text)
    #if d_item['name'] == 'Eventlogger':
        #continue

    #print d_item['name']
    for s_item in sensor:
        if s_item['name'] == "溫度".decode('utf-8'):
            url = 'https://iot.cht.com.tw/iot/v1/device/'+str(d_item['id'])+'/sensor/'+str(s_item['id'])+'/rawdata'
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)
            return data['value'][0]
