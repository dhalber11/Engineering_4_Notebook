#type: ignore
import board
import digitalio
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
import time 

Seconds = 10 

while True:
    if Seconds > 0:
        print("T-Minus",Seconds)
        time.sleep(0.5)
        Seconds = Seconds -1
    else
    print("LIFTOFF")
    time.sleep(.5)
        