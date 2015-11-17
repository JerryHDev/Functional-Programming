#Jerry Huang
#Period 4

def main():
    score = eval(input("Enter your score: "))
    if score <= 100 and score >= 90:
        print("Nice, you got an A")
    if score < 90 and score >=80:
        print("Nice, you got a B")
    if score < 80 and score >= 70:
        print("You got a C")
    if score < 70 and score >= 60:
        print("Good effort, you got a D")
    if score < 60:
        print("You got an F")

main()
