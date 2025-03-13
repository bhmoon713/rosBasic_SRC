#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('move_robot_node')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

move = Twist()


def callback(msg):
    front_range = msg.ranges[len(msg.ranges) // 2]  
    left_range = msg.ranges[int(len(msg.ranges) * 0.9)]  
    right_range = msg.ranges[int(len(msg.ranges) * 0.1)]  


    rospy.loginfo(f"Front: {front_range:.2f}m, Left: {left_range:.2f}m, Right: {right_range:.2f}m")

    if front_range > 1.0 and left_range > 1.0 and right_range > 1.0:
        move_forward() 

    elif front_range < 1.0:  
        turn_left() 

    elif right_range < 1.0:  
        turn_left() 

    pub.publish(move)


def move_forward():
    rospy.loginfo("Moving Forward only")
    move.linear.x = 0.2 
    move.angular.z = 0.0

def turn_left():
    rospy.loginfo("Turning Right only")
    move.linear.x = 0.0
    move.angular.z = 0.5 

rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback)

rospy.spin()
