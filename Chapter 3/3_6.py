def main():
    print("This program calculates the slope of any two points in a plane")
    x1,y1 = eval(input("Enter the first set of two points(x1,y1): "))
    x2,y2 = eval(input("Now enter the second set of two points(x2,y2): "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line through these two sets of points is", slope)
	
main()
