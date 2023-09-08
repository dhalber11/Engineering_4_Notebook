#type: ignore
import board
import digitalio
Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP1)
Rled.direction = digitalio.Direction.OUTPUT
import time 

while True:
    if Seconds > 0:
        print("T-Minus",Seconds)
        time.sleep(0.5)
        Seconds = Seconds -1
        Rled.value = True
        time.sleep(.5)
        Rled.value = False
    else:
        print("LIFTOFF")
        time.sleep(.5)
        