#!/usr/bin/env python3.8
"""
Code for Gazebo class
Author: Shilpaj Bhalerao
Date: Oct 04, 2020
"""

import rospy
import time
from turtlesim.srv import *
from std_srvs.srv import Empty
from gazebo_msgs.msg import *


class Gazebo:
    def __init__(self):
        rospy.init_node("GazeboControl")

        assert sim_time is True, "Set /use_sim_time to True"
        print("ROS Time been used")

        rospy.Subscriber('/lunar_world/set_link_state', gazebo_msgs/LinkState, self.callback_link_states)
        rospy.Subscriber('/lunar_world/set_model_state', gazebo_msgs/ModelState, self.callback_model_states)

        while not rospy.is_shutdown():
            self.pause()
            time.sleep(5)
            self.unpause()
            time.sleep(5)
            self.reset_world()
            time.sleep(5)
            self.reset()
        exit()

    def callback_link_states(self):
        pass

    def callback_model_states(self):
        pass

    def use_sim_time(self):
        rospy.set_param('/use_sim_time', True)

    def pause(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/pause_physics', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def unpause(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/unpause_physics', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def reset(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/reset_simulation', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def reset_world(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/reset_world', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))


# class Model:
#     def __init__(self):
#         self._name =
#
#     def __repr__(self):
#         print("Turtle {}".format(self.name))
#
#     def spawn(self, x, y, theta):
#         """
#         Function to spawn turtles in the Turtle-sim
#         :param x: x-position with respect to origin at bottom-left
#         :type x: float
#         :param y: y-position with respect to origin at bottom-left
#         :type y: float
#         :param theta: orientation with respect to x-axis
#         :type theta: float between [0 to 3] OR [0 to -3]
#         """
#         try:
#             serv = rospy.ServiceProxy('/spawn', Spawn)
#             serv(x, y, theta, self.name)
#         except rospy.ServiceException as e:
#             rospy.loginfo("Service execution failed: %s" + str(e))
#
#     def set_pen(self, flag=True):
#         """
#         Function to sketch the turtle movements
#         :param flag: To turn sketching pen - ON[True]/OFF[False]
#         :type flag: bool
#         """
#         try:
#             if not flag:
#                 set_serv = rospy.ServiceProxy('/' + self.name + '/set_pen', SetPen)
#                 set_serv(0, 0, 0, 0, 1)
#             elif flag:
#                 set_serv = rospy.ServiceProxy('/' + self.name + '/set_pen', SetPen)
#                 set_serv(255, 255, 255, 2, 0)
#         except rospy.ServiceException as e:
#             rospy.loginfo("Service execution failed: %s" + str(e))
#
#     def teleport(self, x, y, theta):
#         """
#         Function to teleport the turtle
#         :param x: x-position with respect to origin at bottom-left
#         :type x: float
#         :param y: y-position with respect to origin at bottom-left
#         :type y: float
#         :param theta: orientation with respect to x-axis
#         :type theta: float between [0 to 3] OR [0 to -3]
#         """
#         try:
#             serv = rospy.ServiceProxy('/' + self.name + '/teleport_absolute', TeleportAbsolute)
#             serv(x, y, theta)
#         except rospy.ServiceException as e:
#             rospy.loginfo("Service execution failed: %s" + str(e))
#
#     def kill_turtle(self):
#         """
#         Function to remove the turtle from Turtle-sim
#         """
#         try:
#             serv = rospy.ServiceProxy('/kill', Kill)
#             serv(self.name)
#         except rospy.ServiceException as e:
#             rospy.loginfo("Service execution failed: %s" + str(e))


if __name__ == '__main__':
    try:
        sim = Gazebo()
    except KeyboardInterrupt:
        exit()
