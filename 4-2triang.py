import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac_gpios = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(dac_gpios, GPIO.OUT)

def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]


try:
    while True:
        for num in list(range(256)) + list(range(255, -1, -1)):
            GPIO.output(dac_gpios[::-1], dec2bin(num))
            time.sleep(0.001)
finally:
    GPIO.output(dac_gpios, 0)
    GPIO.cleanup()