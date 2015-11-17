#Jerry Huang
#Period 3

def main():
    score = eval(input("Enter your score: "))
    gradescore = grade(score)
    print("Your grade is a(n)", gradescore)

def grade(score):
    myList = ["A", "B", "C", "D", "F"]
    if score <= 100 and score >= 90:
        return myList[0]
    if score < 90 and score >=80:
        return myList[1]
    if score < 80 and score >= 70:
        return myList[2]
    if score < 70 and score >= 60:
        return myList[3]
    if score < 60:
        return myList[4]

main()
