#Jerry Huang
#Period 4

def main():
    listNums = input("Enter a string of numbers separated by a comma: ")
    numNums = listNums.split(",")
    answer = toNumbers(numNums)
    print(answer)
    
def toNumbers(strList):
    length = len(strList)
    for i in range(length):
        strList[i] = int(strList[i])
    return strList
        
main()
