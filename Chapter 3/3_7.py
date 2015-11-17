import math
def main():
    print("This program calculates the distance between any two points in a plane")
    x1,y1 = eval(input("Enter the first set of two points(x1,y1): "))
    x2,y2 = eval(input("Now enter the second set of two points(x2,y2): "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between these two points is ", distance, "units")
	
main()
