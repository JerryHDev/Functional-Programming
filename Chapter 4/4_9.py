from graphics import *

def main():
    win = GraphWin("Rectangle Information",400,400)
    text = Text(Point(200,50), "Click two points");text.draw(win)
    perimeter_ = Text(Point(75,300), "Perimeter:");perimeter_.draw(win)
    area_ = Text(Point(250,300), "Area:");area_.draw(win)
    answer_perimeter = Text(Point(115,300),"");answer_perimeter.draw(win)
    answer_area = Text(Point(290,300),"");answer_area.draw(win)
    p1 = win.getMouse();p1.draw(win)
    p2 = win.getMouse();p2.draw(win)
    rect = Rectangle(Point(p1.getX(),p1.getY()),Point(p2.getX(),p2.getY()))
    rect.draw(win)
    width = abs(p1.getX() - p2.getX())
    height = abs(p1.getY() - p2.getY())
    area = height * width
    perimeter = (height * 2) + (width * 2)
    answer_area.setText(area)
    answer_perimeter.setText(perimeter)
    text.setText("Click anywhere to quit")
    win.getMouse()
    win.close()
    
main()


