#type: ignore
import board
import time
import adafruit_mpu6050 
import busio 
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

Rled = digitalio.DigitalInOut(board.GP0)
Rled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)   #initialize the accelerometer
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)    #these three lines are here to initialize the Oled screen
reset = board.GP2
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


splash = displayio.Group()    # this is all initialization code in preparation to print to the oled. Grouping the text and defining each piece
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)  
display.show(splash)  
# text = (f"X acceleration {round(Xaccel, 3)}")
# text_area = label.Label(terminalio.FONT, text= text, color = 0xFFFF00, x=4, y=4)
# splash.append(text_area) 




while True: 
    Xaccel = mpu.acceleration[0]  #sets the X acceleration to the variable and reads it
    Yaccel = mpu.acceleration[1]
    Zaccel = mpu.acceleration[2]

    AngularX = mpu.gyro[0]   #sets the angular velocity to make it easier to print
    AngularY = mpu.gyro[1]
    AngularZ = mpu.gyro[2]

    # print(f"{mpu.acceleration}")
    Xaccel = round(Xaccel, 3)    #rounding all of the variables to 3 decimal places
    Yaccel = round(Yaccel, 3)
    Zaccel = round(Zaccel, 3) 

    text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}" 
    #the line above is the f string that I am printing to the oled. using the round term to get three decimal places on each. 

    # print(f"X acceleration {Xaccel}")   #print all of the accelerations
    # print(f"Y Acceleration {Yaccel}")
    # print(f"Z Acceleration {Zaccel}")
    # print(" ")      # spaces out the printing to make it readable

    time.sleep(.1)

    



    if abs(Xaccel) >= 9.2 or abs(Yaccel) >= 9.2:    #takes the absolute value to not have negatives then when it is at 90
        Rled.value = True   #turns the LED on
        time.sleep(.1) 
    else:
        Rled.value = False  #turns the led off
        