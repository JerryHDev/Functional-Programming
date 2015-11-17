#Jerry Huang
#Period 4

def main():
    print("This program computes the inner product of two lists.")
    print("Press <Enter> when you have finished entering the inputs.")

    x = 0
    y = 0
    xList, yList = [], []
    pair = input("Enter an ordered pair (x,y): ")
    pair = pair.split(",")
    x, y = pair[0], pair[1]
    while x != "":
        y = pair[1]
        xList.append(int(x))
        yList.append(int(y))
        pair = input("Enter the next ordered pair (x,y): ")
        pair = pair.split(",")
        x = pair[0]

    print(innerProd(xList, yList))

def innerProd(xList, yList):
    myList = []
    for i in range(len(xList)):
        myList.append(xList[i] * yList[i])

    total = 0
    for i in range(len(myList)):
        total = total + myList[i]

    return total

main()
    
