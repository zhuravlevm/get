import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
comp = 14
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]   

def bin1(A):
    num = 0
    st = 7
    
    for i in A:
        num += i*2**st
        st-=1     
    return num


def vol_troyka():
    return GPIO.input(comp)*3.3 / 256

def adc1(volt):
    
    one = round((3.3/256), 4)
    Vol = [one*i for i in range(256)]
    return Vol.index(volt)

def adc():
    D = [0 for i in range(8)]
    one = round((3.3/256), 4)
    Vol = [one*i for i in range(256)]
    
    
    for i in range(8):
        D[i] = 1
        
        number = (D)
        GPIO.output(dac, number) 
        time.sleep(0.01)
        #print(bin1(D),GPIO.input(comp) )
        if GPIO.input(comp) == 1:
            D[i] = 0

    
    GPIO.output(dac, D)     
    return Vol[bin1(D)]

def leds(Voltage):
    GPIO.output(leds, Voltage)

try:
    measured = []
    start_time = time.time()
    GPIO.output(troyka, GPIO.HIGH)
    u = vol_troyka()
    
    while adc() <= 0.8 * 3.3:
        measured.append(adc())
        #GPIO.output(leds, dec_bin(adc()))
        time.sleep(0.01)
        #print(measured)
    
    
    GPIO.output(troyka, GPIO.LOW)
    #print(measured)
    plt.plot(measured)
    plt.show()

    while adc() > 0.65 * 3.3:
        measured.append(adc())
        #GPIO.output(leds, dec_bin(adc()))
        time.sleep(0.01)
        #print(measured)
    
    plt.plot(measured)
    plt.show()

    finally_time = time.time()
    Time = finally_time - start_time

    
    
    measured_str = [str(adc1(item)) for item in measured]
    print(measured, measured_str)

    with open('data.txt', 'w') as outfile:
        outfile.write('\n'.join(measured_str))    
    
    
    Quant = 3.3/256
    Vd = 1/(Time/len(measured))
    a = [str(Quant), str(Vd)]
    with open('setting.txt', 'w') as outfile1:
        outfile1.write('\n'.join(a))  
    
    
    print('Общая продолжительность эксперимента: ', Time)
    print('Период: ', Time/len(measured))
    print('Частота дискретизации ', Vd)
    print('Шаг квантования ', Quant)

    


        
except KeyboardInterrupt:
            print('The program was stopped by keyboard')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()