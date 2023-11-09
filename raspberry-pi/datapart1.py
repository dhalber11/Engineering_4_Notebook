#type: ignore
import board
import time
import adafruit_mpu6050 
import busio 
import digitalio



Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

mpu = adafruit_mpu6050.MPU6050(i2c)     #initialize the accelerometer

tilt = 0 
with open("/data.csv", "a") as datalog:
    while True: 
        time_elapsed = time.monotonic()     #sets time to a variable
        Xaccel = mpu.acceleration[0]  #sets the X acceleration to the variable
        Yaccel = mpu.acceleration[1]
        Zaccel = mpu.acceleration[2]


        if abs(Xaccel) >= 9.2 or abs(Yaccel) >= 9.2:    #takes the absolute value to not have negatives then when it is at 90
            Gled.value = True   #turns the LED on
            time.sleep(.1) 
            tilt = 1 
        else:
            Gled.value = False  #turns the led off
            tilt = 0 
            

        datalog.write(f"{Xaccel}, {Yaccel}, {Zaccel}, {time_elapsed}, {tilt}")
        Gled.value = True 
        time.sleep(.5)
        Gled.value = False
        # print(f"X acceleration {Xaccel}")   #print all of the accelerations
        # print(f"Y Acceleration {Yaccel}")
        # print(f"Z Acceleration {Zaccel}")
        # print(" ")      # spaces out the printing to make it readable


        time.sleep(.1)

   
