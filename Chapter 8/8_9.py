#Jerry Huang
#Period 4

def main():
    print("This program computes the fuel efficiency of a multi-leg journey.")
    print("Exit the program by pressing the <Enter> key.")
    odometer = eval(input("Enter the starting odometer reading: "))
    x = 1
    gas = 0
    total_gas = 0
    user_input = input("Enter the current odometer reading and amount of gas used after this leg (separated by a space): ")
    while user_input != "":
        user_input = user_input.split(" ")
        miles_traveled = int(user_input[0]) - odometer
        odometer = int(user_input[0])
        gas_used = int(user_input[1]) - gas
        gas = int(user_input[1])
        MPG = miles_traveled / gas_used
        print("On leg", x, "you achieved", MPG, "miles per gallon")
        x = x + 1
        user_input = input("Enter the current odometer reading and amount of gas used after this leg (separated by a space): ")
        total_miles = odometer
        total_gas = gas
    print("The total miles per gallon for the trip is", total_miles/total_gas)

main()
