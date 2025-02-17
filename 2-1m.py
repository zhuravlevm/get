import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gps = [2, 3, 4, 17, 27, 22, 10, 9]

for i in gps: GPIO.setup(i, GPIO.OUT)

for i in range(3):
        for j in gps:
            GPIO.output(j, 1)
            time.sleep(0.2)
            GPIO.output(j, 0)

for i in gps: GPIO.output(i, 0)

GPIO.cleanup()