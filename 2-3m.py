import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

aux = [22, 23, 27, 18, 15, 14, 3, 2]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(aux, GPIO.IN)

GPIO.setup(leds, GPIO.OUT)
while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

