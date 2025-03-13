#! /usr/bin/env python

import rospy
# from std_msgs.msg import Int32 
from nav_msgs.msg import Odometry

def callback(msg): 
  print (msg.pose.pose.position.x, msg.pose.pose.orientation.x)
#   print (msg.pose.pose.orientation.x)

# rospy.init_node('topic_subscriber')
# sub = rospy.Subscriber('/counter', Int32, callback)

rospy.init_node('odom_sub_node')
sub = rospy.Subscriber('/odom', Odometry, callback)

rospy.spin()