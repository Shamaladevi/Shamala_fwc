from machine import Pin
import time

# Input buttons
A = Pin(2, Pin.IN, Pin.PULL_DOWN)
B = Pin(3, Pin.IN, Pin.PULL_DOWN)
C = Pin(4, Pin.IN, Pin.PULL_DOWN)
D = Pin(5, Pin.IN, Pin.PULL_DOWN)

# Output LED
F = Pin(15, Pin.OUT)

# MUX logic function
def mux_logic(a, b, c, d):
    I = [c, d, int(not c), c & d]
    sel = (a << 1) | b
    return I[sel]

# Main loop
while True:
    a = A.value()
    b = B.value()
    c = C.value()
    d = D.value()
    
    out = mux_logic(a, b, c, d)
    F.value(out)

    print(f"A={a} B={b} C={c} D={d} -> F={out}")
    time.sleep(0.1)
