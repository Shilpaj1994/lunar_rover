#!/usr/bin/env python3.8
"""
Code for Models in Gazebo
Author: Shilpaj Bhalerao
Date: Oct 05, 2020
"""

import rospy
import time
from turtlesim.srv import *
from std_srvs.srv import Empty
from gazebo_msgs.srv import SpawnModel, DeleteModel


class Models:
    def __init__(self, name):
        self._name = name

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

    # def callback_link_states(self):
    #     pass
    #
    # def callback_model_states(self):
    #     pass
    #
    # def use_sim_time(self):
    #     rospy.set_param('/use_sim_time', True)

    def spawn_urdf(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/spawn_urdf_model', SpawnModel)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def spawn_sdf(self):
        """
            Function to Reset the Simulator
        """
        # TO DO: Add model info to the service type and then execute the service
        model_details = SpawnModel()

        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/spawn_sdf_model', SpawnModel)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def delete_model(self):
        """
            Function to Reset the Simulator
        """
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/delete_model', DeleteModel)
            reset_serv(self._name)
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))


if __name__ == '__main__':
    try:
        sim = Models(robot)
    except KeyboardInterrupt:
        exit()
