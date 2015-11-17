def main():
    print("This program determines your distance to a lightning strike.")
    time = eval(input("Enter the amount of time elapsed between the flash and sound of thunder(seconds): "))
    distance = time * 1100
    print("The lightning strike is approximately", distance, "feet away.")
	
main()
