#!/usr/bin/env python

import rospy
from Tkinter import *
#http://effbot.org/tkinterbook/canvas.htm

ROS_RATE=10	 # 10hz


class Nav2DGUI:
    def __init__(self):
        master = Tk()
        w = Canvas(master, width=200, height=100)
        w.pack()

        w.create_line(0, 0, 200, 100)
        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

        w.create_rectangle(50, 25, 150, 75, fill="blue")

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