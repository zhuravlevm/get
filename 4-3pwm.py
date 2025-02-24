import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
a = GPIO.PWM(23, 10000)

a.start(0)

try:
    while True:
        Duty_cycle = (input("Insert the duty cycle "))
        if Duty_cycle == 'q':
            break
        a.start(int(Duty_cycle))
finally:
    GPIO.cleanup()
    