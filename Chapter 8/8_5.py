#Jerry Huang
#Period 4

import math

def main():
    try:
        #gets the value from the user
        print("This program determines if an entered value is prime.")
        value = eval(input("Enter a number: "))

        x = 2
        for i in range((math.sqrt(value) - 2) + 1):
            x = x + 1
            answer = math.sqrt(value) / x
            if answer == int(answer):
                print("The number {0} is not prime".format(value))
            elif answer != int(answer):
                print("The number {0} is not prime".format(value))
    except:
        print("An error occured. Please try again.")

main()
                
