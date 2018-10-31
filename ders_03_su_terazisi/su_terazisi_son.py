from microbit import *

while True:
    deger = accelerometer.get_x()
    if deger > 20:
        display.show(">")
    elif deger < -20:
        display.show("<")
    else:
        display.show("+")