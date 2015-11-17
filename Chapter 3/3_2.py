def main():
print("This program calculates cost per square inch of a circular pizza")
diameter = eval(input("Enter the diameter of the pizza: "))
price = eval(input("Now enter the price of the pizza: "))
A = 3.14 * (diameter/2)**2
x = price/A
print("The cost per square of inch of this pizza is:", x)
	
main()
