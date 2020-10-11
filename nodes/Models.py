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
from gazebo_msgs.msg import *
from geometry_msgs.msg import *


class Models:
    def __init__(self, file, name, position, orientation, ref_frame):
        self._filename = file
        self._name = name
        self._x_pos = position[0]
        self._y_pos = position[1]
        self._z_pos = position[2]
        self._roll = orientation[0]
        self._pitch = orientation[1]
        self._yaw = orientation[2]
        self._ref = ref_frame


    def spawn(self):
        """
        Function to Reset the Simulator
        """
        pos = Pose()
        coor = Point()
        rot = Quaternion()

        coor.x = self._x_pos
        coor.y = self._y_pos
        coor.z = self._z_pos

        rot.x = self._roll
        rot.y = self._pitch
        rot.z = self._yaw
        rot.w = 0.0

        pos.position = coor
        pos.orientation = rot

        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/spawn_sdf_model', SpawnModel)
            reset_serv(self._name, self._filename, '', pos, self._ref)
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
        husky_address = "/home/shilpaj/ROS_ws/src/sim/model/husky/model.sdf"
        husky_lidar_address = "/home/shilpaj/ROS_ws/src/sim/model/husky_lidar/model.sdf"

        with open(husky_lidar_address, "r") as f:
            filename = f.read()
            print("Model loaded", type(filename))
        name = 'husk'
        position = [10, 10, 0]
        orientation = [0, 0, 0]
        ref_frame = 'world'

        husky = Models(filename, name, position, orientation, ref_frame)
        husky.spawn()
    except KeyboardInterrupt:
        exit()
