#!/usr/bin/env python
# This line will ensure the interpreter used is the first one on your environment's $PATH. Every Python file needs
# to start with this line at the top.

import rospy # Import the rospy, which is a Python library for ROS.
import time # Import the time module for time-related functions

rospy.init_node('ObiWan_inPy') # Initiate a node called ObiWan

print("Help me Obi-Wan Kenobi, you're my only hope") # A simple Python print

time.sleep(10) # Pause the program for 10 seconds

# This code will print the message after 10 seconds of waiting.