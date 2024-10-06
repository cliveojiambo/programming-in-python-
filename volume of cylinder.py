import math

def volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def main():

    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    
    volume = volume_of_cylinder(radius, height)
 
    print(f"The volume of the cylinder is: {volume:.2f}")

if __name__ == "__main__":
    main()
