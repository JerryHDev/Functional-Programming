def main():
    print("This program computes the nth Fibonacci number")
    z = 1
    a = 0
    b = 0
    x = eval(input("Enter the nth Fibonacci number: "))
    for i in range(x-1):
        b = a
        a = z
        z = a + b
    print(z)
main()
