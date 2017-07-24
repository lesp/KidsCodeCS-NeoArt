from microbit import *
import neopixel
from random import randint
np = neopixel.NeoPixel(pin0, 47)

while True:
    for i in range(24):
        np[i] = (randint(0,30),randint(0,30),randint(0,30))
        np.show()
        sleep(100)
    for i in range(24,40):
        np[i] = (randint(0,30),randint(0,30),randint(0,30))
        np.show()
        sleep(100)
    for i in range(40,47):
        np[i] = (randint(0,30),randint(0,30),randint(0,30))
        np.show()
        sleep(100)