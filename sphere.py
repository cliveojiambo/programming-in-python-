import math

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3


def main():

    radius = float(input("Enter the radius of the sphere: "))
  
    volume = volume_of_sphere(radius)
   
    print(f"The volume of the sphere is: {volume:.2f}")

if __name__ == "__main__":
    main()
