import requests
import json
import uuid
import time

host_url = "http://iottalk.tw:9999/"
mac_address = "%x" % uuid.getnode()
device_name = "M1"
device_model_name = "meichuhackathon"
user_name = "yb"
is_simulation = False;
device_feature_list = ["JsonReceiver"]

request_headers = {
  "content-type": "application/json"
}

request_body = {
  "profile": {
    "d_name": device_name,
    "dm_name": device_model_name,
    "u_name": user_name,
    "is_sim": is_simulation,
    "df_list": device_feature_list
  }
}

def register_on_IoTtalk():
  global request_body, request_headers, host_url, mac_address
  response = requests.post(host_url + mac_address,
      data = json.dumps(request_body), timeout = 2, headers = request_headers)
  print response.status_code
  print response.text

def deregister_on_IoTtalk():
  global host_url, mac_address
  response = requests.delete(host_url + mac_address)
  if str(response.status_code)[0] == "4":
    print response.text
  elif str(response.status_code)[0] == "5":
    print "fail"
  else:
    pass

def push_data_to_IoTtalk(request_data, idf):
  global host_url, mac_address, request_headers
  response = requests.put(host_url + mac_address + '/%s' %(idf),
      data = json.dumps({"data": [ request_data ]}), headers = request_headers)
  if str(response.status_code)[0] == "4":
    print response.text
  elif str(response.status_code)[0] == "5":
    print "push data fail"
  else:
    pass
'''
register_on_IoTtalk()
time.sleep(5)
push_data_to_IoTtalk({"test-data": "111"}, "JsonReceiver")
time.sleep(3)
deregister_on_IoTtalk()
'''
