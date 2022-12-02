import requests
import json
import smbus
import time
from datetime import datetime

projectId = "2C3ti7yXc1nkKH6WNlNrrT13VKF"
projectSecret = "0e905e5ebd6c5aa010bb00fdb2ee8869"
endpoint = "https://ipfs.infura.io:5001"

# Get I2C bus
bus = smbus.SMBus(1)

# MCP9808 address, 0x18(24)
# Select configuration register, 0x01(1)
# 0x0000(00)	Continuous conversion mode, Power-up default
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
# MCP9808 address, 0x18(24)
# Select resolution rgister, 0x08(8)
# 0x03(03)	Resolution = +0.0625 / C
bus.write_byte_data(0x18, 0x08, 0x03)

time.sleep(0.5)

# MCP9808 address, 0x18(24)
# Read data back from 0x05(5), 2 bytes
# Temp MSB, TEMP LSB
data = bus.read_i2c_block_data(0x18, 0x05, 2)

# Convert the data to 13-bits
ctemp = ((data[0] & 0x1F) * 256) + data[1]
if ctemp > 4095:
    ctemp -= 8192
ctemp = ctemp * 0.0625
ftemp = ctemp * 1.8 + 32

# Output data to screen
# string = "Temperature in Celsius is " + str(ctemp)
#print("Temperature in Celsius is    : %.2f C" +  str(ctemp))
#print("Temperature in Fahrenheit is : %.2f F" +  str(ftemp))

data = {
    "temperature": ctemp,
    "timestamp": datetime.now().timestamp(),
}


files = {
    'file': json.dumps(data)
}

response = requests.post(endpoint + '/api/v0/add',
                         files=files, auth=(projectId, projectSecret))
p = response.json()
hash = p['Hash']
print(hash)

hash = str(hash)

parameters = {
    'device_id': 'dev-1',
    'ipfs_hash': hash,
    'device_key': 'OGqwsyc8u8'
}

response = requests.put(
    "http://34.193.203.14:8080/iot/ipfs-hash/", json=parameters)
print(response)
data = response.text
json = json.loads(data)
print(json)
