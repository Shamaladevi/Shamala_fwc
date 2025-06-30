 from machine import Pin
import time

# Define input pins (buttons)
A = Pin(2, Pin.IN, Pin.PULL_DOWN)
B = Pin(3, Pin.IN, Pin.PULL_DOWN)
C = Pin(4, Pin.IN, Pin.PULL_DOWN)

# Define output pin (LED for F)
F = Pin(15, Pin.OUT)

while True:
    # Read inputs
    a = A.value()
    b = B.value()
    c = C.value()
    
    # Logic implementation:
    g1 = a and b             # AND gate
    g2 = b or c              # OR gate
    g3 = not g2              # NOT gate
    f = g1 or g3             # Final OR gate

    # Output to LED
    F.value(int(f))
    
    # Optional: debug print
    print(f"A={a} B={b} C={c} => F={int(f)}")
    
    time.sleep(0.1)
