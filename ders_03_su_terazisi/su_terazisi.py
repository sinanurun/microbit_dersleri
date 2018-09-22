# Add your Python code here. E.g.
from microbit import *


while True:
    deger = accelerometer.get_x()
    if deger > 20:
        display.scroll("Sag")
    elif deger < -20 :
        display.scroll("sol")
    else:
        display.scroll("Denge")