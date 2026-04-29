from machine import Pin
import time


led_pins = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 28, 27]
leds = [Pin(p, Pin.OUT) for p in led_pins]


row_pins = [26, 22, 21, 20]
col_pins = [19, 18, 17, 16]
rows = [Pin(p, Pin.OUT) for p in row_pins]
cols = [Pin(p, Pin.IN, Pin.PULL_DOWN) for p in col_pins]

keys = [['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]

def scan_keypad():
    for r_idx, r_pin in enumerate(rows):
        r_pin.value(1)
        for c_idx, c_pin in enumerate(cols):
            if c_pin.value() == 1:
                r_pin.value(0)
                return keys[r_idx][c_idx]
        r_pin.value(0)
    return None

while True:
    key = scan_keypad()
    if key:
        if key == '1': leds[0].value(1)
        elif key == '2': leds[1].value(1)
        elif key == '3': leds[2].value(1)
        elif key == '4': leds[3].value(1)
        elif key == '5': leds[4].value(1)
        elif key == '6': leds[5].value(1)
        elif key == '7': leds[6].value(1)
        elif key == '8': leds[7].value(1)
        elif key == '9': [l.value(1) for l in leds[:8]]
        elif key == '0': [l.value(0) for l in leds[:8]]
        elif key == 'A': leds[8].value(1)
        elif key == 'B': leds[9].value(1)
        elif key == 'C': leds[10].value(1)
        elif key == 'D': leds[11].value(1)
        elif key == '*': [l.value(1) for l in leds[8:]]
        elif key == '#': [l.value(0) for l in leds[8:]]
        time.sleep(0.2)
    time.sleep(0.01)
