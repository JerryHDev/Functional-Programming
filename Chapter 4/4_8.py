from graphics import *
import math

def main():
    win = GraphWin("Line Segment Info", 400,400)
    win.setCoords(0,0,400,400)
    intro = Text(Point(200,375),"Click two points");intro.draw(win)
    Text(Point(50,60),"Length:").draw(win)
    Text(Point(220,60),"Slope:").draw(win)
    length = Text(Point(130,60),"");length.draw(win)
    slope = Text(Point(300,60),"");slope.draw(win)
    p1 = win.getMouse();p1.draw(win)
    p2 = win.getMouse();p2.draw(win)
    line = Line(p1,p2);line.draw(win)
    length_ = math.sqrt((abs(p1.getX() - p2.getX()))**2 + (abs(p1.getY() - p2.getY()))**2)
    slope_ = (p1.getY() - p2.getY()) / (p1.getX() - p2.getX())
    length.setText(length_)
    slope.setText(slope_)
    intro.setText("Click anywhere to quit")
    win.getMouse()
    win.close()
    
main()
