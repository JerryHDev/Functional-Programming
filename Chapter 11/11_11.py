#Jerry Huang
#Period 4

def main():
    print("This program automatically censors four-letter words in a file.")

    fileName = input("Enter the file name: ")
    outputfileName = input("Enter the file name for the censored text to go in: ")

    infile = open(fileName, "r")
    outfile = open(outputfileName, "w")

    for line in infile:
        myList = line.split()
        for i in range(len(myList)):
            if len(myList[i]) == 4:
                print("****", end = " ", file=outfile)
            else:
                print(myList[i], end = " ", file = outfile)

main()
