#Jerry Huang
#Period 4

def main():
    print("This program can perform a variety of operations on a list.")
    user_input = input("Enter a list of objects separated by a comma: ")
    startList = user_input.split(", ")
    print()
    print("1. Count")
    print("2. Is in")
    print("3. Index")
    print("4. Reverse")
    print("5. Sort")
    a = eval(input("Select which list operation you want to use: "))
    print("--------------------------------------------------")
    if a == 1:
        #Count function
        print("\nYou have selected the count operation, which")
        print("counts how many of an object is in the list.")
        x = input("Enter what you would like to count the number of: ")
        n = count(startList, x)
        print(n)
    if a == 2:
        #IsIn function
        print("\nYou have selected the Is In operation, which")
        print("determines whether an object is in the list.")
        x = input("Enter what you would like to test if it is in the list: ")
        y = isin(startList, x,)
        print(y)
    if a == 3:
        #Index function
        print("\nYou have selected the index operation, which")
        print("determines the position of an object in the list.")
        x = input("Enter the object that you want to find the position of: ")
      
        position = index(startList, x)
        print("The position of the object you entered is {0}".format(position))
    if a == 4:
        #Reverse function
        print("\nYou have selected the reverse operation, which")
        print("reverses the order of all the objects in the list.")
        reverse(startList)
    if a == 5:
        #Sort function
        print("\nYou have selected the sort operation, which sorts")
        print("the objects in the list from least to greatest.")
        sort(startList)

def count(startList, x):
    n = 0
    for i in startList:
        if x == i:
            n = n + 1
    return n

def isin(startList, x):
    y = "Yes"
    n = "No"
    for i in startList:
        if x == i:
            return y
    return n

def index(startList, x):
    a = 0
    while str(x) != str(startList[a]):
        a = a + 1
        position = a
    return position

def reverse(startList):
    length = len(startList)
    for i in range(length):
        

        
            
            
        


main()
        
