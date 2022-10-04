import requests
import json


parameters = {
    'device_id' : 'dev1',
    'device_key': 'abcd'
}


response = requests.put("http://10.0.0.120:5000/iot/data-access", json = parameters)
print(response)
data = response.text
json = json.loads(data)
print(json)