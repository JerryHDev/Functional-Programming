def main():
print("This program calculates the volume and surface area of a sphere")
x = eval(input("Enter the radius of the sphere: "))
V = 4/3 * 3.14 * (x**3)
SA = 4 * 3.14 * (x**2)
print("The volume is", V, "and surface area is", SA)
	
main()
