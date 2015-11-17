def main():
	print("This program determines the length of a ladder required to reach a given height")
	input_height, input_angle = eval(input("Enter the length of ladder and the angle of the	ladder(degrees) separated by a comma: "))
	radians = input_angle/180
	length = input_height/radians
	print("The length of this ladder is", length)
	
main()
