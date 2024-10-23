from machine import Pin
import time

# Setup GPIO pins
data_pin = Pin(20, Pin.OUT)  
clock_pin = Pin(18, Pin.OUT)  
latch_pin = Pin(19, Pin.OUT)  
oe_pin = Pin(21, Pin.OUT)  

oe_pin.value(0)  # Enable output

def shift_out(value):
    for i in range(16):
        data_pin.value(value >> (15 - i) & 1)
        clock_pin.value(1)
        clock_pin.value(0)

def update_leds(value):
    latch_pin.value(0)
    shift_out(value)
    latch_pin.value(1)

while True:
    for i in range(16):
        update_leds(1 << i)
        time.sleep(0.5)
