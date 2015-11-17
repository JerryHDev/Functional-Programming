import graphics
from graphics import*
def main():
    win = GraphWin()
    center = Point(100,100)
    circle5 = Circle(center, 75)
    circle4 = Circle(center, 60)
    circle3 = Circle(center, 45)
    circle2 = Circle(center, 30)
    circle1 = Circle(center, 15)
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

main()
    
