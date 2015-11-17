#Jerry Huang
#Period 4

def main():
    try:
        
        n = eval(input("Enter the nth Fibonacci number: "))
        number = fib(n)
        print("The", n, "th Fibonacci number is", number)
    except:
        print("An error occured.")
def fib(n):
    try:
        
        a,b = 1, 1
        for i in range(n-1):
            a, b = b, a + b
        return a
    except:
        print("An error occured.")
        
main()

    
