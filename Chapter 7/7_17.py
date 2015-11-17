#Jerry Huang
#Period 4

from graphics import *

def main():

    #creates the ball in the graphics window
    win = GraphWin("Bouncy Ball", 500,500)
    win.setCoords(0,0,500,500)
    x = 100
    y = 100
    ball = Circle(Point(x, y), 100)
    ball.setFill("red")
    ball.draw(win)
    dx = 5
    dy = 5
    
    #waits for mouse click before starting animation
    win.getMouse()

    for i in range(10000):
        ball.move(dx, dy)
        x = x + dx
        y = y + dy
        #when the x value reaches 400, reverse movement in x direction
        if x == 400:
            dx = -1 * dx
        else:
            dx = dx
            
        #when y value reaches 400, reverse movement in y direction
        if y == 400:
            dy = -1 * dy
        else:
            dy = dy

        #when ball reaches back to starting point, reverse direction again
        if x == 100:
            dx = -1 * dx
        else:
            dx = dx
        if y == 100:
            dy = -1 * dy
        else:
            dy = dy
    

    #closes window upon mouse click
    win.getMouse()
    win.close()

main()
