
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


    if area == 0:
        continue


# Success message
    else:
        print(f"The area of the triangle with vertices {val1}, {val2}, {val3} is {area} square km")










