#Jerry Huang
#Period 4

def main():
    print("This program will determine your elegibility for the Senate and House.")
    age = eval(input("Enter your age: "))
    citizen = eval(input("Enter your years of citizenship: "))
    if age >= 30:
        if citizen >= 9:
            print("You are eligible for the Senate and House.")
        if (citizen < 9) and (citizen >=7):
            print("You are eligible for the House.")
    if (age < 30) and (age >= 25):
        if citizen >= 7:
            print("You are eligible for the House.")
    else:
        print("You are not eligible for the Senate and House.")

main()
