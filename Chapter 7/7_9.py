#Jerry Huang
#Period 4

def main():
    print("This prints out the date of Easter of the year entered.")
    
    year = eval(input("Enter a year in the range 1982 - 2048, inclusive: "))

    try:
        a = year%19
        b = year%4
        c = year%7
        d = (19 * a + 24)%30
        e = (2 * b + 4 * c + 6 * d + 5)%7
        value = d + e
        if value > 9:
            value = value - 9
            print("Easter is on April " + str(value))
        elif value <= 9:
            value = value + 22
            print

    except:
        print("Error, make sure you entered a year within the range 1982 - 2048.")

main()
        
