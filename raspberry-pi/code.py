
#type: ignore
import board
import digitalio
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
import time 

while True: 
    led.value = True
    time.sleep(0.5)
    led.value = False