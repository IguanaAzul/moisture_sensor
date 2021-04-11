import requests

url = 'http://192.168.100.33/sensor/register/'

post = {'sensor_id': "jesus", "sensor_name": "suculenta", "chat_id": "IguanaAzul"}
print(requests.post(url, json=post))
