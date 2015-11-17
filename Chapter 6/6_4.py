#Jerry Huang
#Period 4

def main():
    n1 = eval(input("Enter a number to calculate: "))
    a = sumN(n1)
    b = sumNCubes(n1)
    print("The sum of the first n natural numbers is:", str(a))
    print("The sum of the cubes of the first n natural numbers is:", str(b))

def sumN(n):
    x = 0
    y = 0
    for i in range(n):
        x = x + 1
        y = y + x
    return y

def sumNCubes(n):
    z = 0
    x = 0
    y = 0
    for i in range(n):
        x = x + 1
        z = (x)**3
        y = y + z
    return y

main()
