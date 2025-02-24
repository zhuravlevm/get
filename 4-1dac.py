import RPi.GPIO as GPIO

def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]

def voltage(a):
    return 3.3 / 255 * a

GPIO.setmode(GPIO.BCM)

dac_gpios = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(dac_gpios, GPIO.OUT)

try:
    while True:

        while True:
            f = 0
            n = (input("Введите целое число от 0 до 255 "))
            if n == 'q': break

            try:
                n = int(n)
            except ValueError:
                f = 1
                if type(n) == float:
                    print("Введено не целое число")
                else:
                    print("Введено не числовое значение")
            if f == 0 and n < 0:
                print("Введено отрицательное число")
                f = 1
            if f == 0 and n not in range(0, 256):
                print("Введено значение превышающее возможности 8-битового ЦАП")
                f = 1
            if f == 0: break

        if n == 'q':
            break

        GPIO.output(dac_gpios[::-1], dec2bin(int(n)))
        print(voltage(int(n)), 'В')
finally:
    GPIO.output(dac_gpios, 0)
    GPIO.cleanup()
