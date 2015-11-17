#Jerry Huang
#Period 4

def main():
    print("This program calculates the future value of investment.")
    principal = eval(input("Enter the initial value: "))
    apr = eval(input("Enter the annual interest rate: "))
    y = eval(input("Enter the number of years for the investment: "))

    #creates chart
    print("")
    print("{0:^1} {1:^10}".format("Year", "Value"))
    print("-----------------")
    numYear = 0
          
    #iterates through future value
    for i in range(y):
        principal = principal * (1 + apr)
        print("{0:^3} ${1:<10.2f}".format(numYear, principal))
        numYear = numYear + 1

main()
              
