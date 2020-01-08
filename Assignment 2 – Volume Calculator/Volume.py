#importing the necessary tools for the ellipsoid
import math
from math import pi

#This is the function for calculating the volume of a cube, it ask for specific dimentions and it can calculate the volume.
def cube():
    a = int(input("Side length:"))
    volume = a**3
    return volume
#This is the function for calculating the volume of a pyramid, it ask for specific dimentions and it can calculate the volume.
def pyramid():
    b = int(input("Base length of the pyramid:"))
    h = int(input("Height length of the pyramid:"))
    volume = (1/3)*(b**2)*(h)
    return volume
#This is the function for calculating the volume of a ellipsoid it uses pi which is kinda different from the other two.
def ellipsoid():
    r1 = int(input("The first radius:"))
    r2 = int(input("The second radius:"))
    r3 = int(input("The third radius:"))
    volume = 4/3*pi*r1*r2*r3
    return volume
