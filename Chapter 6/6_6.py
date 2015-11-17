#Jerry Huang
#Period 4

def main():
    a = eval(input("Enter the value of the first side: "))
    b = eval(input("Enter the value of the second side: "))
    c = eval(input("Enter the value of the third side: "))
    area = valueS(a, b, c)
    print("The area of this triangle is", area)
    myFile = open("6_6.py", "w")
    print("The area is", area, file = myFile)

def valueS(a, b, c):
    s = (a + b + c)/2
    return s

main()
    
    
    
    
