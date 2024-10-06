import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def main():
  
    radius = float(input("Enter the radius of the circle: "))
 
    area = area_of_circle(radius)

    print(f"The area of the circle is: {area:.2f}")

if __name__ == "__main__":
    main()
