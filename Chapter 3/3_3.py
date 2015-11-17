def main():
print("This program determines the molecular weight of a hydrocarbon")
input_hydrogen = eval(input("Enter the number of hydrogen atoms: "))
	input_carbon = eval(input("Enter the number of carbon atoms: "))
	input_oxygen = eval(input("Enter the number of oxygen atoms: "))
	weight = (input_hydrogen * 1.0079) + (input_carbon * 12.011) + (input_oxygen * 15.9994)
	print("The total weight is", weight)
	
main()
