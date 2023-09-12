#type: ignore
import board
import digitalio
Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP1)
Rled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP 
import time 

Seconds = 10    #Define the variable 
Bpress = 0      #Define the buttons variable

while True:
    if button.value == False:   #when the button is pressed
        Bpress = 1              #change the button to pressed for the whole countdown
    if Seconds > 0 and Bpress ==1:
        print("T-Minus",Seconds)  #Print the countdown
        time.sleep(0.5)
        Seconds = Seconds -1    #reduce the variable by 1 each time
        Rled.value = True    #turn the red led on
        time.sleep(.5)       #pause 1/2 second
        Rled.value = False  #turn the red led off, blinking it
    if Seconds <= 0:           #when it hits zero 
        print("LIFTOFF")    #print LIFTOFF when variable is 0
        Gled.value = True   #turn the green led on to indicate liftoff
        time.sleep(.5)
        Bpress = 0         #Resetting the variable