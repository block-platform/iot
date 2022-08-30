import requests
import json

projectId = "2C3ti7yXc1nkKH6WNlNrrT13VKF"
projectSecret = "0e905e5ebd6c5aa010bb00fdb2ee8869"
endpoint = "https://ipfs.infura.io:5001"

files = {
'file': ('Congrats! You have uploaded your file to IPFS!'),
}

#response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
response = requests.post(endpoint + '/api/v0/add', files=files, auth=(projectId, projectSecret))
p = response.json()
hash = p['Hash']
print(hash)

