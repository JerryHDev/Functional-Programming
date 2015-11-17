def main():
    print("This program will determine the average of a set of numbers")
    z = 0
    numbers = eval(input("First, enter how numbers you will enter: "))
    for i in range(numbers):
        x = eval(input("Enter number: "))
        x = x + z
        z = x
    average = z / numbers
    print("The average of these numbers is", average)
	
main()
