import requests
import json
import datetime
import DAN.DAN as DAN
import IoT

output_data={
	'on':None,
	'id':None,
	'location_school':None,
	'status_school':None,
	'object_school':None,
	'temperature':None,
	'number':None
	}
locat= [	
	"SecondRestaurant",
	"FirstRestaurant",
	"GirlsSecondRestuarant",
	"ED202",
	"MIRC311",
	"McD",
	"KFC",
	"BK"
]





def parse(input_data):
	global output_data
	for i in range(len(input_data['queryResult']['parameters'].keys())):
		print(i)
		if input_data['queryResult']['parameters'].keys()[i] == "object_311onoff":
			output_data['id'] = input_data['queryResult']['parameters']['object_311onoff']
		elif input_data['queryResult']['parameters'].keys()[i] == "action_on-off":
			output_data['on'] = input_data['queryResult']['parameters']['action_on-off']
		elif input_data['queryResult']['parameters'].keys()[i] == "location_school":
			output_data['location_school'] = input_data['queryResult']['parameters']['location_school']
		elif input_data['queryResult']['parameters'].keys()[i] == "status_school":
			output_data['status_school'] = input_data['queryResult']['parameters']['status_school']
		elif input_data['queryResult']['parameters'].keys()[i] == "object_school":
			output_data['object_school'] = input_data['queryResult']['parameters']['object_school']
		elif input_data['queryResult']['parameters'].keys()[i] == "number":
			output_data['number'] = input_data['queryResult']['parameters']['number']
		elif input_data['queryResult']['parameters'].keys()[i] == "temperature":
			output_data['temperature'] = input_data['queryResult']['parameters']['temperature']

def SendParse(output_data):
	request_headers={
		"CK": "DKR95B0TT0XT2K5PF9",
		"Content-Type": "application/json"
	}
	if output_data['id'] != None:
		send_dict = {'id':output_data['id'], 'on':output_data['on']}
		DAN.push_data_to_IoTtalk(send_dict,"JsonReceiver")
	elif output_data['object_school']!= None and output_data['temperature']!= None and output_data['location_school']!= None and output_data['number']!= None:
		send_dict= {'id': output_data['location_school']+"_"+output_data['object_school']+"_"+"controller"+"_"+str(output_data['number']), 'time':datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'), 'lat':"", 'lon':"", 'save': "true", 'value': [str(output_data['temperature']['amount'])]}
		test = [send_dict]
		print (test)
		r=requests.post('https://iot.cht.com.tw/iot/v1/device/10722883951/rawdata', data = json.dumps(test), headers = request_headers)
		if r.status_code == requests.codes.ok:
			msg= "Your %s has been set!" % output_data['object_school']
			responseMsg={
				'fulfillmentText':msg
			}
		else:
			msg = "Something Error!"
			responseMsg={
				'fulfillmentText':msg
			}	
		return responseMsg

	elif output_data['location_school']!=None and output_data['location_school']!="" and output_data['status_school']!=None:
		try:
			locatIndex=locat.index(output_data['location_school'])
			locatTemp=IoT.temperature(locatIndex)
			print locatTemp
			responseMsg={
				'fulfillmentText': "The Temperature of "+locat[locatIndex]+" is "+locatTemp+" degress"
			}
			print (responseMsg)
		except:
			print("It's not in Location List")	
			responseMsg={
				'fulfillmentText':"It's not in Location List"
			}
		
		
		return responseMsg
	else:
		responseMsg={
			"fulfillmentText": "Something Error, please try again"
		}
		print ("Error")
		return responseMsg
		



