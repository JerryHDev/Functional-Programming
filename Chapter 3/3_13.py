def main():
    z = 0
    print("This program that sums a series of numbers entered by the user.")
    n = eval(input("Enter the number of numbers to be summed: "))
    for i in range(n):
        y = eval(input("Enter next number: "))
        y = y + z
        z = y
    print("The sum of the numbers is", y)
    
main()
