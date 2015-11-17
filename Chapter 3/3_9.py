import math
def main():
	print("This program calculates the area of a triangle")
	a, b, c = eval(input("Enter the lengths of three sides separated by commas: "))
	s = (a + b + c)/2
	A = math.sqrt(s * (s - a) * (s - b) * (s - c))
	print("The area of the triangle is", a)
	
main()
