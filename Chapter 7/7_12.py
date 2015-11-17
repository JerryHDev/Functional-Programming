#Jerry Huang
#Period 4

def main():
    print("This program will determine if a date is valid.")
    userInput = input("Enter the date in the form month/day/year: ")

    #gets value for month, day, and year
    month, day, year = userInput.split("/")

    #first 3 if statements are baseline restrictions on dates
    if int(month) < 1 or int(month) > 12:
        print("This is an invalid date.")
    if int(day) > 31 or int(day) < 1:
        print("This is an invalid date.")
    if int(year) < 1:
        print("This is an invalid date.")

    #sets restrictions on months with less than 31 days
    if int(month) == 2:
        if int(day) > 28:
            print("This is an invalid date.")
    if int(month) == 4:
        if int(day) > 30:
            print("This is an invalid date.")
    if int(month) == 6:
        if int(day) > 30:
            print("This is an invalid date.")
    if int(month) == 9:
        if int(day) > 30:
            print("This is an invalid date.")
    if int(month) == 11:
        if int(day) > 30:
            print("This is an invalid date.")

    #any month with 31 days
    else:
        print("This is a valid date.")

main()
