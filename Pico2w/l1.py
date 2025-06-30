from machine import Pin
import time

# Inputs
btn_a = Pin(2, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Outputs
led_or  = Pin(15, Pin.OUT)  # P (OR)
led_and = Pin(14, Pin.OUT)  # Q (AND)
led_nor = Pin(13, Pin.OUT)  # R (NOR)
led_xor = Pin(12, Pin.OUT)  # S (XOR)

while True:
    a = btn_a.value()
    b = btn_b.value()

    # Logic gates
    or_out  = a | b
    and_out = a & b
    nor_out = not (a | b)
    xor_out = a ^ b

    # Output to LEDs
    led_or.value(or_out)
    led_and.value(and_out)
    led_nor.value(int(nor_out))  # cast bool to int
    led_xor.value(xor_out)

    time.sleep(0.1)

