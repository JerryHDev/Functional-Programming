#Jerry Huang
#Period 3

def main():
    listNums = input("Enter a list of numbers separated by a comma: ")
    numNums = listNums.split(",")
    answer = squareEach(numNums)
    print(answer)
    
def squareEach(nums):
    length = len(nums)
    for i in range(length):
        nums[i] = (int(nums[i])**2)
    return nums
        
main()
