#Jerry Huang
#Period 4

def main():
    n = eval(input("Enter the nth Fibonacci number: "))
    number = fib(n)
    print("The", n, "th Fibonacci number is", number)

def fib(n):
    a,b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a



main()
