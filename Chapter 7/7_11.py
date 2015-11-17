#Jerry Huang
#Period 4

def main():
    print("This program will determine whether a year is a leap year")
    
    year = eval(input("Enter a year: "))

    #tests for century year
    centuryYear = year / 100
    if centuryYear == int(centuryYear):
        if centuryYear / 400 == int(centuryYear):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

    #if not a century year:
    else:
        if year / 4 == int(year / 4):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

main()
