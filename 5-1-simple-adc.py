import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)


def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]


def adc():

    start = time.time()

    for value in range(256):
        GPIO.output(dac, dec2bin(value))
        time.sleep(0.001)

        compValue = GPIO.input(comp)

        if compValue == 1:
            dtime = time.time() - start
            return [value, dtime]
    
    dtime = time.time() - start
    return [256, dtime]


try:

    while True:
        
        results = adc()
        voltage = results[0] * 3.3 / 256

        print(voltage, f' time spent - {results[1]}')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()