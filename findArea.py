
from __future__ import print_function
import math



def calculateArea():
    shape = str(input("Enter the shape Circle/Rectange/Square : "))
    shape = shape.lower()
    area = None
    if ('circle' in shape):
        area = circle()
        print ("The area of the circle is %.2f" %area)
    elif ('rectangle' in shape):
        area = rectangle()
        print ("The area of the Rectangle` is %.2f" %area)
    elif ('square' in shape):
        area = square()
        print ("The area of the Square is %.2f" %area)
    else:
        print ("Enter a valid shape")




def circle():
    radius = int ( input("Enter the radius of the circle :"))
    area = math.pi * math.pow(radius,2)
    return area

def rectangle():
    length = int (input("Enter the Length of the rectangle :"))
    bredth = int (input("Enter the Breadth of the rectangle :"))
    area = length * bredth
    return area

def square():
    side = int(input("Enter side of the square : "))
    area = math.pow(side,2)
    return int(area)


calculateArea()


