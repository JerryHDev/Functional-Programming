from graphics import *
import math

def main():
    #gets circle radius
    win = GraphWin("Circle Intersection", 400,400)
    win.setCoords(-10,-10,10,10)
    user_r = Text(Point(-2,1), "Enter radius of circle:");user_r.draw(win)
    input = Entry(Point(3,1),5)
    input.setText("0.0")
    input.draw(win)
    rect = Rectangle(Point(-3,-3),Point(3,-5))
    rect.setFill("light blue")
    rect.draw(win)
    button = Text(Point(0,-4),"Continue")
    button.draw(win)
    win.getMouse()
    input.undraw()
    r = eval(input.getText())
    #gets y-int
    button.setText("Graph")
    user_r.setText("Enter y-intercept:")
    input = Entry(Point(3,1),5)
    input.setText("0.0")
    input.draw(win)
    win.getMouse()
    y_int = eval(input.getText())
    user_r.undraw()
    input.undraw()
    button.undraw()
    rect.undraw()

    #graph
    circle = Circle(Point(0,0), r);circle.draw(win)
    line = Line(Point(-10,y_int),Point(10,y_int));line.draw(win)
    #points of intersection
    x_int = math.sqrt((r**2) - (y_int**2))
    print("The two points of intersection are", -x_int,",",y_int, "and", x_int,",", y_int)
    #graphing points of intersection
    point1 = Point(-x_int,y_int)
    point1.setFill("red")
    point1.draw(win)
    point2 = Point(x_int,y_int)
    point2.setFill("red")
    point2.draw(win)

main()
