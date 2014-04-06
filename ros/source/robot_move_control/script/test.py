#!/usr/bin/env python
# -*- coding: utf-8 -*
import rospy

rospy.init_node("joystike")

r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
	print "hi"
	r.sleep()

