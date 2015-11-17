#Jerry Huang
#Period 4

def main():
    print("This program illustrates a chaotic function.")
    input_1 = eval(input("Enter a number between 0 and 1: "))
    input_2 = eval(input("Enter another number between 0 and 1: "))
    numIterations = eval(input("Enter the number of iterations: "))

    #creates chart
    print("")
    print("{0:^1} {1:^7} {2:^10}".format("index", input_1, input_2))
    print("-----------------------")
    numIndex = 1
    #iterates through the chaos function
    for i in range(numIterations):
        input_1 = 3.9 * input_1 * (1 - input_1)
        input_2 = 3.9 * input_2 * (1 - input_2)
        print("{0:^3} {1:^10} {2:^15}".format(numIndex, input_1, input_2))

main()
