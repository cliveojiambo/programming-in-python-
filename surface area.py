surface area
C:\Users\user\PycharmProjects\programming in python\pythonProject\surface area.py
import math

def surface_area_of_cylinder(radius, height):
    surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    return surface_area


radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))


surface_area = surface_area_of_cylinder(radius, height)


print(f"The surface area of the cylinder is: {surface_area:.2f} square units")
