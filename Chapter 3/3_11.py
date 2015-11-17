def main():
    fact = 0
    n = eval(input("Enter a number: "))
    for number in range(n+1):
        fact = fact + number
    print(fact)
	
main()
