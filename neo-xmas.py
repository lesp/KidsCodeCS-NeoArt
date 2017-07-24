from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 47)

while True:
    for i in range(0,24,2):
        np[i] = (30,0,0)
        np.show()
        sleep(100)
    for i in range(1,24,2):
        np[i] = (0,30,0)
        np.show()
        sleep(100)
    for i in range(24,40,2):
        np[i] = (30,30,0)
        np.show()
        sleep(100)
    for i in range(25,40,2):
        np[i] = (0,30,0)
        np.show()
        sleep(100)
    for i in range(40,47,2):
        np[i] = (30,30,30)
        np.show()
        sleep(100)
    for i in range(41,47,2):
        np[i] = (30,30,0)
        np.show()
        sleep(100)
    sleep(1000)
#Animation
    for i in range(0,24,2):
        np[i] = (0,0,30)
        np.show()
        sleep(100)
    for i in range(1,24,2):
        np[i] = (30,0,30)
        np.show()
        sleep(100)
    for i in range(24,40,2):
        np[i] = (30,30,30)
        np.show()
        sleep(100)
    for i in range(25,40,2):
        np[i] = (0,0,30)
        np.show()
        sleep(100)
    for i in range(40,47,2):
        np[i] = (30,30,0)
        np.show()
        sleep(100)
    for i in range(41,47,2):
        np[i] = (30,0,0)
        np.show()
        sleep(100)
    sleep(1000)