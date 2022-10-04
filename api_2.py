import requests
import json

str = str("ABCD")


parameters = {
    'device_id' : 'dev1',
    'ipfs_hash' : str,
    'device_key': 'abcd'
}

response = requests.put("http://127.0.0.1:5000/iot/ipfs-hash", json = parameters)
print(response)
data = response.text
json = json.loads(data)
print(json)