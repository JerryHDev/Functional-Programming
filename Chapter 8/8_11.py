#Jerry Huang
#Period 4

def main():
    print("This program computes the running total of cooling and heating degree-days.")
    user_input = input("Enter a sequence of average daily temperatures separated by a comma: ")
    user_input = user_input.split(",")
    length = len(user_input)
    x = 0
    cooling = 0
    heating = 0
    for i in range(length):
        if int(user_input[x]) < 60:
            difference = 60 - int(user_input[x])
            heating = heating + difference
        if int(user_input[x]) > 80:
            difference = int(user_input[x]) - 80
            cooling = cooling + difference
        x = x + 1
            
    print("The cooling degree-day temp is", cooling, "degrees")
    print("The heating degree-day temmp is", heating, "degrees")

main()
