# Kyle Stowe
# 2/18/25
# P2LAB1
# Program that calculates the diameter, circumference and area of a circle

import math

radius = float(input("What is the radius of the circle? "))
diameter = radius * 2
circumference = 2 * radius * math.pi
area = math.pi * math.pow(radius,2)
print("")

print(f"The Diameter of the circle is {diameter:.1f}\n")
print(f"The Circumference of the circle is {circumference:.2f}\n")
print(f"The Area of the circle is {area:.3f}\n")
