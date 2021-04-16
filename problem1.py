#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math 
def hypotenuse(a,b,boolean):
    c = math.sqrt(a**2 + b**2)

    if boolean == True and a**2 + b**2 == c**2:
        return c
    elif boolean == False and a > b:
        return math.sqrt(a**2 - b**2)
    elif boolean == False and a < b:
        return math.sqrt(b**2 - a**2)