# Triangle related math

# Finding 3rd angle if other 2 angle are given
angle1 = int(input("Enter first angle : "))
angle2 = int(input("Enter second angle : "))

angle3 = 180 - (angle1 + angle2)

print("The 3rd angle is : ", angle3)

# Finding area of a triangle

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle : "))

area = 0.5 * base * height

print("The area of the triangle is : ", area)

# Area of an equilateral traingle

side = int(input("Side value of an equilateral triangle : "))

from math import sqrt

area_equi_triangle = (sqrt(3) / 4) * (side ** 2)

print("The area of that equilateral triangle is : ", area_equi_triangle)

