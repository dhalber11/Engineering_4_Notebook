import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import busio 
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 


display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)    #these three lines are here to initialize the Oled screen
reset = board.GP2
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash = displayio.Group()

area = 0 

text_area = label.Label(terminalio.FONT, text=area, color=0xFFFF00, x=5, y=5)
splash.append(text_area)  
display.show(splash)  


def TriArea(x1,y1,x2,y2,x3,y3): #Creates a function to find the area
    try: #Find the area if coordinates are valid
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) #Triangle area formula
        return area
    except: #If coordinates are invalid
        print("Invalid Coordinates")
        area = 0
        return area

while True:
    print("Point 1 Coordinates (x,y):") #Print so the perwson running code knows which coordinates
    p1 = input() #Return whatever the user types in
    x1, y1 = p1.split(",") #Turn p1 into two variables separated by a comma
    print(f"Point 1: ({p1})") #Confirm the coordinates

    print("Point 2 Coordinates (x,y):") #Repeat for coordinate 2
    p2 = input()
    x2, y2 = p2.split(",")
    print(f"Point 2: ({p2})")

    print("Point 3 Coordinates (x,y):") #Repeat for coordinate 3
    p3 = input()
    x3, y3 = p3.split(",")
    print(f"Point 3: ({p3})")

    x1 = float(x1) #Turn varibles from strings into floats so they can be plugged into the function
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    
    area = TriArea(x1,y1,x2,y2,x3,y3) #Plug in floats to find area
    print(" ")
    print(f"AREA IS: {area}")
    print(" ")

    hline = Line(0,32,128,32, color=0xFFFF00)  #show the horizontal line for the grid on the OLED
    splash.append(hline)
    vline = Line(64, 0, 64, 64, color=0xFFFF00)     #show the vertical line on the grid
    splash.append(vline)

    X1 = int(x1+64)     # Change all of the floats into iterable variables for the OLED
    X2 = int(x2+64)
    X3 = int(x3+64)
    Y1 = int(32-y1)
    Y2 = int(32-y2)
    Y3 = int(32-y3)


    circle = Circle(64, 32, 3, outline=0xFFFF00)    #show the OLED how to print a circle
    splash.append(circle)

    triangle = Triangle(x1, y1, x2, y2, x3, y3, outline=0xFFFF00)   #show OLED how to use the points for a triangle
    splash.append(triangle)


