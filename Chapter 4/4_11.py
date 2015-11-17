from graphics import *
def main():
    win = GraphWin("Five-click House",600,600)
    win.setCoords(0,0,600,600)
    title = Text(Point(300,575),"First, click the bottom left corner of the house, then top right")
    title.draw(win)
    
    #house frame
    house_corner_1 = win.getMouse();house_corner_1.draw(win)
    house_corner_2 = win.getMouse();house_corner_2.draw(win)
    house_frame = Rectangle(house_corner_1,house_corner_2)
    house_frame.draw(win)
    title.setText("Now click the center of the top edge of the door")

    #door
    width_house = (house_corner_2.getX() - house_corner_1.getX())
    door_top = win.getMouse()
    door_top.getX()
    door_left = Point((door_top.getX()) - 1/6 * width_house, door_top.getY())
    Line(door_top,door_left).draw(win)
    door_right = Point((door_top.getX()) + 1/6 * width_house, door_top.getY())
    Line(door_top,door_right).draw(win)
    door_bottom_left = Point((door_top.getX()) - 1/6 * width_house, house_corner_1.getY())
    door_bottom_right = Point((door_top.getX()) + 1/6 * width_house, house_corner_1.getY())
    Line(door_left,door_bottom_left).draw(win)
    Line(door_right,door_bottom_right).draw(win)
    title.setText("Now click the center of a square window")

    #window
    center = win.getMouse()
    width_window = (door_top.getX() - door_left.getX()) / 2
    window_topright = Point((center.getX() + width_window), (center.getY() + width_window))
    window_topleft = Point((center.getX() - width_window), (center.getY() + width_window))
    window_bottomright = Point((center.getX() + width_window), (center.getY() - width_window))
    window_bottomleft = Point((center.getX() - width_window), (center.getY() - width_window))
    Line(window_topright,window_topleft).draw(win)
    Line(window_topleft,window_bottomleft).draw(win)
    Line(window_bottomleft,window_bottomright).draw(win)
    Line(window_bottomright,window_topright).draw(win)
    title.setText("Now click a point for the peak of the roof")

    #roof
    peak = win.getMouse()
    house_topright = Point(house_corner_2.getX(), house_corner_2.getY())
    house_topleft = Point(house_corner_1.getX(), house_corner_2.getY())
    Line(house_topleft,peak).draw(win)
    Line(house_topright,peak).draw(win)
    title.setText("Complete! Click anywhere to quit")
    win.getMouse()
    win.close()

main()
