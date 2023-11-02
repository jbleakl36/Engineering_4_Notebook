# type:ignore
# Establishing shapes for the OLED
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import terminalio
import adafruit_mpu6050
import busio
import board
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
displayio.release_displays()
splash = displayio.Group()
sda_pin = (board.GP10) #Assinging the location of the pin
scl_pin = (board.GP11)
i2c = busio.I2C(scl_pin, sda_pin) # establishing i2c
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP12)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # Defining OLED Screen


def triangle_area(x1y1, x2y2, x3y3):
    try:
    
        #Establishing variables
        x1y1 = x1y1.split(",")
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")

        x1 = x1y1[0]
        y1 = x1y1[1]
        x2 = x2y2[0]
        y2 = x2y2[1]
        x3 = x3y3[0]
        y3 = x3y3[1]
        
        x1 = float(x1)
        y1 = float(y1) 
        x2 = float(x2)
        y2 = float(y2)
        x3 = float(x3)
        y3 = float(y3)
# Calculation for area
        area=  abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

        return area
# Error message
    except:
        print("incompatable syntax detected, please try again >:(")


        area = 0
        return area



while True:
# Prompt for the inputs
    val1 = input("Enter the first coordinate values of x,y: ")
    val2 = input("Enter the second coordinate values of x,y: ")
    val3 = input("Enter the first coordinate values of x,y: ")

    area = triangle_area(val1, val2, val3)
    title = (f"{area}")
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)
# Defining values
    x1y1 = val1.split(",")
    x2y2 = val2.split(",")
    x3y3 = val3.split(",")
    x1 = x1y1[0]
    y1 = x1y1[1]
    x2 = x2y2[0]
    y2 = x2y2[1]
    x3 = x3y3[0]
    y3 = x3y3[1]
    x = 62
    y = 32
    r = 2

    if area == 0:
        continue


# Success message
    else:
        hline = Line(0,32,128,32, color=0xFFFF00) #Creating line
        splash.append(hline)
        hline = Line(64,0,64,64, color=0xFFFF00) #Creating line
        splash.append(hline)
        circle = Circle(x, y, r, outline=0xFFFF00) #Creating circle
        splash.append(circle)
        triangle = Triangle((int(x1)+64), (int(y1)+32), (int(x2)+64), (int(y2)+32), (int(x3)+64), (int(y3)+32), outline=0xFFFF00) #Creating Triangle
        splash.append(triangle) # Making the triange real
        display.show(splash)

        print(f"The area of the triangle with vertices {val1}, {val2}, {val3} is {area} square km")










