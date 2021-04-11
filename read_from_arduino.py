import serial
import requests
import time

url = 'https://9c8a66cbd3b9.ngrok.io/sensor/moisture/'
arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1000)
arr = list()
sensor_id = "12"

t0 = 21600
while True:
    read = arduino.readline()
    # print(float(read))
    if float(read) < 50 and time.time() - t0 >= 21600:
        post = {"sensor_id": sensor_id, "umidade": float(read)}
        print(requests.post(url, json=post).json())
        t0 = time.time()
