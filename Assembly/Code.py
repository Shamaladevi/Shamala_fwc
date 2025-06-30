from machine import Pin

import time



# Define input pins with pull-down resistors

x = Pin(0, Pin.IN, Pin.PULL_DOWN)

y = Pin(1, Pin.IN, Pin.PULL_DOWN)

z = Pin(2, Pin.IN, Pin.PULL_DOWN)



# Output pin for LED

f = Pin(15, Pin.OUT)



while True:

    # Read input states

    x_val = x.value()

    y_val = y.value()

    z_val = z.value()

    

    # Logic: F = (NOT X AND NOT Y) OR (Y AND Z)

    not_x = 1 - x_val

    not_y = 1 - y_val

    

    and1 = not_x and not_y

    and2 = y_val and z_val

    

    f_val = and1 or and2



    # Set LED state

    f.value(f_val)



    # Optional: print for debugging

    print(f"X={x_val}, Y={y_val}, Z={z_val} => F={f_val}")

    

    time.sleep(0.6)
