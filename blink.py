from machine import Pin
import time

led = Pin('LED', Pin.OUT)
btnAdd = Pin(12, Pin.IN, Pin.PULL_DOWN)
btnSub = Pin(14, Pin.IN, Pin.PULL_DOWN)
number = 0


while True:
    if btnAdd.value():
        number += 1
        print(number)
        time.sleep(0.5)
    print('.')
    led.toggle()
    time.sleep(0.2)
    led.toggle()
    time.sleep(0.2)
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)
    print('/')