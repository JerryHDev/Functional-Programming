from graphics import *

def main():
    #gets principal input
    win = GraphWin('Investment Growth Chart', 320, 240)
    text = Text(Point(130,120),"Principal:")
    text.draw(win)
    input = Entry(Point(220,120),10)
    input.setText('0.0');input.draw(win)
    rect = Rectangle(Point(130,180), Point(190,220))
    rect.setFill('light blue')
    rect.draw(win)
    button = Text(Point(160, 200), 'Continue')
    button.draw(win)
    win.getMouse()
    principal = eval(input.getText())
    text.undraw()
    input.undraw()
    rect.undraw()
    button.undraw()

    #gets annual interest rate
    text2 = Text(Point(130,120), "Annual interest:")
    text2.draw(win)
    input = Entry(Point(220,120), 10)
    input.setText('0.0');
    input.draw(win)
    rect2 = Rectangle(Point(130,180), Point(190,220))
    rect2.setFill('light blue')
    rect2.draw(win)
    button2 = Text(Point(160,200), 'Graph')
    button2.draw(win)
    win.getMouse()
    apr = eval(input.getText())
    text2.undraw()
    input.undraw()
    rect2.undraw()
    button2.undraw()
    
    #code for graph
    label1 = Text(Point(20, 230), ' 0.0K').draw(win)
    label2 = Text(Point(20, 180), ' 2.5K').draw(win)
    label3 = Text(Point(20, 130), ' 5.0K').draw(win)
    label4 = Text(Point(20, 80), ' 7.5K').draw(win)
    label5 = Text(Point(20, 30), '10.0K').draw(win)
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
    for year in range(1,11):
        principal = principal * (1 + apr)
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11 + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    #quiting program
    rect = Rectangle(Point(280,210), Point(320,230))
    rect.setFill('light blue')
    rect.draw(win)
    button = Text(Point(300,220), 'Quit')
    button.draw(win)
    win.getMouse()
    win.close()

main()

