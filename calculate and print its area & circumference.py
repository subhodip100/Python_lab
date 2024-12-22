'''Problem 1 :
 Write a program to take the diamater of a circle as user input
 and calculate and print its area & circumference.
 lab_8506_week 1_day 1_12_17_2024'''

import math
#taking diameter from user
diameter = float(input("Enter the diameter of the circle :"))
#calculate the radius
radius = diameter/2

#calculate the area & circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

#print result

print(f"The area of circle is : {area : .2f}")
print(f"The circumference of the circle : {circumference :.2f}")

