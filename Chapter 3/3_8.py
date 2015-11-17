def main():
	print("This program determines the Gregorian epact")
	year = eval(input("Enter a 4-digit year: "))
	C = year//100
	epact = (8 + (C//4) - C + ((8 * C + 13)//25) + 11 * (year%19))%30
	print(epact)
	
main()
