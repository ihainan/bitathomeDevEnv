#!/usr/bin/env python
# -*- coding: utf-8 -*

import  os
import  sys
import copy
import roslib
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Joy

# 全局变量
cmd = Twist()		# 运动信息
joy = Joy()		# 手柄信息
pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist)
isButtonDown = False	# 是否按下了按键

# 手柄控制
def joyStrckControl():
	global joy
	walk_vel_ = 0.5
	yaw_rate_ = 1.0
	max_tv = walk_vel_
	max_rv = yaw_rate_

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		# 前进
		if len(joy.axes) == 0:
			rate.sleep()
			continue
		elif joy.axes[1] == 1.0 :
			max_tv = walk_vel_
			speed = 1
			turn = 0
		# 后退
		elif joy.axes[1] == -1.0:
			max_tv = walk_vel_
			speed = -1
			turn = 0
		# 左旋
		elif joy.axes[0] == 1.0:
			max_rv = yaw_rate_
			speed = 0
			turn = 1
		# 右旋
		elif joy.axes[0] == -1.0:
			max_rv = yaw_rate_
			speed = 0
			turn = -1
		# 静止
		else:
			max_tv = walk_vel_
			max_rv = yaw_rate_
			speed = 0
			turn = 0

		cmd.linear.x = speed * max_tv
		cmd.angular.z = turn * max_rv
		print "%f %f %f %f %f %f" % (cmd.linear.x, cmd.linear.y, cmd.linear.z, cmd.angular.x, cmd.angular.y, cmd.angular.z)
		pub.publish(cmd)
		rate.sleep()

# 回调函数
def callback(data):
	global joy
	joy = copy.deepcopy(data)
	return

	
if __name__ == "__main__":
	rospy.init_node("joystike_control")
	rospy.Subscriber("/joy", Joy, callback)
	joyStrckControl()

