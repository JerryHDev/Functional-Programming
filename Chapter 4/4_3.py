import graphics
from graphics import*
def main():
    win = GraphWin("Face")
    face = Circle(Point(100,100), 100)
    face.setFill('dark red')
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
