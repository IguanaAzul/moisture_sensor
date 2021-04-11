import serial
import requests
import time

url = 'http://192.168.100.33/sensor/moisture/'
arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1000)
arr = list()
sensor_id = "jesus"

t0 = 21600
while True:
    read = arduino.readline()
    post = {"sensor_id": sensor_id, "umidade": float(read)}
    if float(read) < 50 and time.time() - t0 >= 21600:
        print(requests.post(url, json=post).json())
        t0 = time.time()
