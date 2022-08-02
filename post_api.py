import requests
import json

files = {
'file': ('Congrats! You have uploaded your file to IPFS!'),
}

response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
p = response.json()
hash = p['Hash']
print(hash)