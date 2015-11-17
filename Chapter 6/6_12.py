#Jerry Huang
#Period 3

def main():
    listNums = input("Enter a list of numbers separated by a comma: ")
    numNums = listNums.split(",")
    answer = sumList(numNums)
    print(answer)
    
def sumList(nums):
    length = len(nums)
    sum = 0
    for i in range(length):
        sum = sum + int(nums[i])
    return sum
        
main()
