import requests

params = (
   ('arg', 'QmWsZ5Um3WzvJHoA6nVVLJ2vCCcKLYSwjJnWcL7Ypgps49'),
)

response = requests.post('https://ipfs.infura.io:5001/api/v0/block/get', params=params)

print(response.text)