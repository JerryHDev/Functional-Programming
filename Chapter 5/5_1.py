#Jerry Huang
#Period 4

def main():
    day, month, year = eval(input("Enter day, month, and year numbers: "))
    months = ["January", "Febuary", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month - 1]
    print("The date is {0}/{1}/{2} or, {3} {1}, {2}".format(month, day, year, monthStr))

main()
