#Jerry Huang
#Period 4

from graphics import *

def main():
    win = GraphWin("Circle Mover", 400, 400)
    circle = Circle(Point(200,200), 100)
    circle.setFill("black")
    circle.setOutline("yellow")
    circle.draw(win)
    text = Text(Point(200,380), "Click a point to move the circle to")
    text.draw(win)
    for i in range(10):
        mouse_click = win.getMouse()
        circle.undraw()
        center = Point(mouse_click.getX(), mouse_click.getY())
        circle = moveTo(circle, center)
        circle.draw(win)
        
                    
def moveTo(shape, newCenter):
    circle = Circle(newCenter, 100)
    circle.setFill("black")
    circle.setOutline("yellow")
    return circle

main()
