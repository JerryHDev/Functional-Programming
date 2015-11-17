#Jerry Huang
#Period 4

from graphics import *

def main():
    center_x = eval(input("Enter the x-value of the center point: "))
    center_y = eval(input("Enter the y-value of the center point: "))
    center = Point(center_x, center_y)
    size = eval(input("Enter the size you want the face to be: "))
    win = input("Enter the name of the Graphics Window: ")
    drawFace(center, size, win)

def drawFace(center, size, win):
    win = GraphWin(win)
    face = Circle(center, size)
    face.setFill('yellow')
    leftCornea = Circle(Point(70,50), 15)
    leftCornea.setFill("blue")
    leftEye = Circle(Point(70, 50), 25)
    leftEye.setFill("white")
    rightCornea = leftCornea.clone()
    rightCornea.move(60,0)
    rightEye = leftEye.clone()
    rightEye.move(60,0)
    face.draw(win)
    leftEye.draw(win)
    leftCornea.draw(win)
    rightEye.draw(win)
    rightCornea.draw(win)
    mouth = Rectangle(Point(70,150),Point(130,170))
    mouth.draw(win)
    mouth.setFill("white")

main()

    
