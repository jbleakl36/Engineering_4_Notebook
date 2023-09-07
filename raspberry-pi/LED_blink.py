# type: ignore
import time #element of time used to stop the led 
import digitalio #led origin
import board #Letting the system know where the led is
led = digitalio.DigitalInOut(board.LED) # Confirmation
led.direction = digitalio.Direction.OUTPUT # Led is activated

while True:    
    led.value = True # it's on
    time.sleep(1) #delay
    led.value = False # it's off
    time.sleep(1) # delay