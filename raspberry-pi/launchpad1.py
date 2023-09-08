#type: ignore
import board
import digitalio
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
import time 

Seconds = 10  #Define the variable to count down from

while True:
    if Seconds > 0:    #if the countdown has not already hit zero then do this
        print("T-Minus",Seconds)  #print the countdown
        time.sleep(0.5)     #pause 1/2 second
        Seconds = Seconds -1  #actually reduce the variable by 1
    else: 
        print("LIFTOFF")  #when seconds is less than 0 print LIFTOFF
        time.sleep(.5)
        