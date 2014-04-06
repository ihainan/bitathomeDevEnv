#!/usr/bin/env python
#-*-encoding:utf-8-*-
# Filename : ihainan
# Created Date : 2014/4/5 09:21
# Description : 控制机器人运动
# Author : ihainan
# E-mail : ihainan72@gmail.com
# Website: www.ihainan.me

import rospy
import math
from robot_move_control.srv import *
from geometry_msgs.msg import *

# 服务接口 - 控制机器人前进特定距离
def handle_control_robot_move_forward(req):
	rospy.loginfo("Move forward %s" % (req.distance))

	# 向模拟器发送消息，控制机器人运动
	pub = rospy.Publisher("cmd_vel_mux/input/teleop", Twist)
	cmd = Twist()
	cmd.linear.x = req.distance
	pub.publish(cmd)
	
	# 服务返回
	return moveForwardResponse(req.distance)
	
# 服务接口 - 控制机器人左右运动特定距离
def handle_control_robot_move_horizontal(req):
	rospy.loginfo("Move Horizontal %s" % (req.distance))

	# 向模拟器发送消息，控制机器人运动
	pub = rospy.Publisher("cmd_vel_mux/input/teleop", Twist)
	cmd = Twist()
	cmd.linear.y = req.distance
	pub.publish(cmd)
	
	# 服务返回
	return moveForwardResponse(req.distance)

# 服务接口 - 控制机器人旋转特定距离
def handle_control_robot_rotate(req):
	rospy.loginfo("Rotate %s" % (req.distance))

	# 向模拟器发送消息，控制机器人运动
	pub = rospy.Publisher("cmd_vel_mux/input/teleop", Twist)
	cmd = Twist()
	cmd.angular.z = math.pi
	pub.publish(cmd)

	# 服务返回
	return moveForwardResponse(req.distance)


# 程序入口
if __name__ == "__main__":
	rospy.init_node("robot_move_control")									# 初始化 node
	s = rospy.Service("control_robot_move_forward", moveForward, handle_control_robot_move_forward)		# 服务接口，用于控制机器人前进运动
	s = rospy.Service("control_robot_move_horizontal", moveForward, handle_control_robot_move_horizontal)	# 服务接口，用于控制机器人左右运动
	s = rospy.Service("control_robot_rotate", moveForward, handle_control_robot_rotate)			# 服务接口，用于控制机器人旋转运动
	rospy.spin()												# 等待直到节点被关闭


