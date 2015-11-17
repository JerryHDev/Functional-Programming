#Jerry Huang
#Period 4

import math

def main():
    radius = eval(input("Enter the radius: "))
    area1 = sphereArea(radius)
    volume1 = sphereVolume(radius)
    print("The surface area of the sphere is", + area1)
    print("and the volume of the sphere is:", + volume1)


def sphereArea(radius):
    A = 4 * math.pi * radius ** 2
    return A

def sphereVolume(radius):
    V = (4/3) * math.pi * radius ** 3
    return V

main()
