#Jerry Huang
#Period 4

def main():
   
    print("This program calculates the total wages for the week.")
    hours = eval(input("Enter the total number of hours you worked this week: "))
    rate = eval(input("Enter the hourly rate: "))
    if hours <= 40:
        money_earned = hours * rate
        print("You earned ${0} for the week".format(money_earned))
    if hours > 40:
        extra_hours = hours - 40
        extra_money = extra_hours * (rate * 1.5)
        normal_money = 40 * rate
        total_money = extra_money + normal_money
        print("You earned ${0} for the week".format(total_money))


main()
