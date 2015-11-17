#Jerry Huang
#Period 4

import math

def main():
  
    #gets the value from the user
    print("This program determines if an entered value is prime.")
    value = eval(input("Enter a number: "))        
    #if number is greater than 2
    while value > 2:
        x = 2
        number = "prime"
        while number == "prime" and x <= math.sqrt(value):
            if value % x == 0:
                number = "not prime"              
            else:
                x = x + 1                
            
        if number == "prime":
            print(value, end = " ")
        value = value - 1
    if value == 2:
        print(value, end = " ")                    
main()
