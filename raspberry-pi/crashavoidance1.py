#type: ignore
import board
import time
import adafruit_mpu6050 
import busio 


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

mpu = adafruit_mpu6050.MPU6050(i2c)     #initialize the accelerometer

while True: 
    Xaccel = mpu.acceleration[0]  #sets the X acceleration to the variable and reads it
    Yaccel = mpu.acceleration[1]
    Zaccel = mpu.acceleration[2]

    # print(f"{mpu.acceleration}")
    print(f"X acceleration {Xaccel}")   #print all of the accelerations
    print(f"Y Acceleration {Yaccel}")
    print(f"Z Acceleration {Zaccel}")
    print(" ")      # spaces out the printing to make it readable

    time.sleep(.1)