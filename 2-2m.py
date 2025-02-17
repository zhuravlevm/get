import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

num = [1, 0, 0, 0, 1, 1, 0, 1]
gps = [8, 11, 7, 1, 0, 5, 12, 6]
for i in gps:
    GPIO.setup(i, GPIO.OUT)

c = 0

for i in gps:
    GPIO.output(i, num[c])
    c += 1
    
time.sleep(30)

for i in gps: GPIO.output(i, 0)

GPIO.cleanup()
