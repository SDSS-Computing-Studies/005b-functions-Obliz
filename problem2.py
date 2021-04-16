#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(c1,c2):
   return round(math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2), 3)