import serial
import requests
import time

url = 'https://localhost:5000/moisture'
arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1000)
arr = list()

t0 = time.time()
while True:
    read = arduino.readline()
    post = {'umidade': float(read)}
    print(post)
    if float(read) < 50 and time.time() - t0 >= 21600:
        requests.post(url, data=post)
        t0 = time.time()
