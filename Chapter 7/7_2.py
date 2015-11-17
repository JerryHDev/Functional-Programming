#Jerry Huang
#Period 4

def main():
    print("This program will determine your grade.")
    x = eval(input("Enter your quiz score (0-5): "))
    if x == 5:
        print("Goodjob, you got an A!")
    if x == 4:
        print("Goodjob, you got a B!")
    if x == 3:
        print("You got a C")
    if x == 2:
        print("You got a D")
    if x == 1 or 0:
        print("F, better luck next time")
    else:
        print("Make sure you've entered a nunber between 0 and 5.")


main()
    
