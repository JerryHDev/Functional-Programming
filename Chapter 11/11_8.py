#Jerry Huang
#Period 4

def main():
    print("This program removes duplicate values from a list.")
    x = input("Enter a list of objects separated by a comma, no space: ")
    somelist = x.split(",")
    print(removeDuplicates(somelist))

def removeDuplicates(somelist):
    newList = []
    for i in somelist:
        if i not in newList:
            newList.append(i)
    return newList
            
            

main()
