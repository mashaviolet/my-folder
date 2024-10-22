#using a function create a program that calculate the volume of a cylinde
def volume_of_cylinder():
 radius= int(input('Enter the radius of a cylinder :'))
 height=int(input('Enter the height of a cylinder :'))
 import math
 pie=math.pi
 volume=pie *radius**2 *height
 print(volume)
volume_of_cylinder() 