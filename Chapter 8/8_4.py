#Jerry Huang
#Period 4

def main():
    print("This program applies the Syracuse sequence to a given number.")
    value = eval(input("Enter a starting value: "))
    while value != 1:
        if value % 2 == 0:
            value = value/2
            print(int(value), end = " ")
        else:
            value = (3 * value) + 1
            print(int(value), end = " ")

main()
    
