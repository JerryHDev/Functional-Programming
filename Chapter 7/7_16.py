#Jerry Huang
#Period 4

from graphics import *
import math

def main():
    #draws the archery target
    win = GraphWin("Archery Scorer", 400, 400)
    win.setCoords(0,0,400,400)
    archeryCenter = Point(200,200)
    circle5 = Circle(archeryCenter, 150)
    circle4 = Circle(archeryCenter, 120)
    circle3 = Circle(archeryCenter, 90)
    circle2 = Circle(archeryCenter, 60)
    circle1 = Circle(archeryCenter, 30)
    circle5.setFill('white')
    circle4.setFill('black')
    circle3.setFill('blue')
    circle2.setFill('red')
    circle1.setFill('yellow')
    circle5.draw(win)
    circle4.draw(win)
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)
    Text(Point(200, 375), "Click 5 places on the archery target to represent arrow shots").draw(win)
    
    score = 0
    finalScore = 0
    
    #loop gives user 5 clicks
    for i in range(5):
        #gets the user click
        userClick = win.getMouse();userClick.draw(win)
        
        #gets distance between archeryCenter and the click using the distance formula
        distance = math.sqrt(((abs(userClick.getX() - archeryCenter.getX()))**2) + ((abs(userClick.getY() - archeryCenter.getX()))**2))
        
        #compares the distance of click from archeryCenter with radius to determine score
        if distance <= 30:
            score = 9
            print("9 points, bulls-eye")
        if (distance > 30) and (distance <= 60):
            score = 7
            print("7 points")
        if (distance > 60) and (distance <= 90):
            score = 5
            print("5 points")
        if (distance > 90) and (distance <= 120):
            score = 3
            print("3 points")
        if (distance > 120) and (distance <= 150):
            score = 1
            print("1 point")
        if (distance > 150):
            Text(Point(200,25), "Make sure you click inside the archery target").draw(win)
            
        #tallies up the score after each click
        finalScore = finalScore + score
    print("You final score is", finalScore, "points")

main()
