def main():
    print("This program calculates the cost of your order.")
    pound = eval(input("Enter the weight of your order: "))
    shipping = pound * 0.86
    cost = pound * 10.50
    total_cost = shipping + cost + 1.50
    print("Your order costs a total of", total_cost, "dollars")
	
main()
