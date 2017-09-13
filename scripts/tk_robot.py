#!/usr/bin/env python

import rospy
from Tkinter import *
#http://effbot.org/tkinterbook/canvas.htm

ROS_RATE=10	 # 10hz


class Nav2DGUI:
    def __init__(self):
        master = Tk()
        self.WIDTH = WIDTH = 500
        self.HEIGHT = HEIGHT = 500
	self.WALL_WIDTH = WALL_WIDTH = 3

        w = Canvas(master, width=WIDTH, height=HEIGHT)
        w.pack()

        w.create_line(0, WALL_WIDTH - 1, WIDTH, WALL_WIDTH - 1, fill="green", width=WALL_WIDTH)
        w.create_line(0, HEIGHT - (WALL_WIDTH - 1), int(WIDTH / 3), HEIGHT - (WALL_WIDTH - 1), fill="green", width=WALL_WIDTH)
        w.create_line(int(2 * WIDTH / 3), HEIGHT - (WALL_WIDTH - 1), WIDTH, HEIGHT - (WALL_WIDTH - 1), fill="green", width=WALL_WIDTH)

        w.create_line(WALL_WIDTH - 1, 0, WALL_WIDTH - 1, HEIGHT, fill="green", width=WALL_WIDTH)
        w.create_line(WIDTH - 1, 0, WIDTH - 1, HEIGHT, fill="green", width=WALL_WIDTH)

        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

        w.create_rectangle(50, 25, 150, 75, fill="blue")
	w.create_polygon(400, 200, 200, 300, 390, 440, 300, 300)

        def exit_ros():
            if rospy.is_shutdown():
                master.quit()
            master.after(ROS_RATE, exit_ros)
        master.after(ROS_RATE, exit_ros)
        mainloop()

if __name__ == '__main__':
    rospy.init_node('robot_2Dnav', anonymous=True)
    rate = rospy.Rate(ROS_RATE)
    gui = Nav2DGUI()