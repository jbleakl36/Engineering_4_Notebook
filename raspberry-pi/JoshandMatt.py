#type:ignore
import time
import adafruit_mpu6050 # importing various programs
import busio
import board
import digitalio
sda_pin = (board.GP14) #Assinging the location of the pin
scl_pin = (board.GP15)
i2c = busio.I2C(scl_pin, sda_pin) # establishing i2c
mpu = adafruit_mpu6050.MPU6050(i2c) # connecting i2c to pico
RedLED = digitalio.DigitalInOut(board.GP2) # Confirmation
RedLED.direction = digitalio.Direction.OUTPUT # Led is activated
RedLED.value = False
with open("/data.csv", "a") as datalog:

    while True:
        RedLED.value = True
        time.sleep(.1)
        RedLED.value = False
        elapsed_time = time.monotonic()# save time to a variable 
        datalog.write(f"{elapsed_time}, {mpu.acceleration:.3f}\n")
        # add a short on/off cycle for your onboard LED
        datalog.flush()
        time.sleep(0.5)
