#Jerry Huang
#Period 4

def main():
    score = eval(input("Enter your score: "))
    myList = ["A", "B", "C", "D", "F"]
    #Mr. Friedland said ok to use if statement for this
    if score <= 100 and score >= 90:
        print("Nice, you got an", myList[0],".")
    if score < 90 and score >=80:
        print("Nice, you got a", myList[1],".")
    if score < 80 and score >= 70:
        print("Nice you got a", myList[2],".")
    if score < 70 and score >= 60:
        print("Good effort, you got a", myList[3],".")
    if score < 60:
        print("Ouch, you got an", myList[4],".")

main()
