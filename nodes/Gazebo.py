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
from gazebo_msgs.srv import *
from geometry_msgs.msg import *


class Gazebo:
    def __init__(self):
        rospy.init_node("GazeboControl")

        self.max_update_rate = 100

        # rospy.Subscriber('/lunar_world/set_link_state', gazebo_msgs/LinkState, self.callback_link_states)
        # rospy.Subscriber('/lunar_world/set_model_state', gazebo_msgs/ModelState, self.callback_model_states)

        while not rospy.is_shutdown():
            self.pause()
            time.sleep(5)
            self.unpause()
            time.sleep(5)
            self.set_moon_physics()
            time.sleep(10)
            self.reset_world()
            time.sleep(5)
            self.reset()
        exit()

    # def callback_link_states(self):
    #     pass

    # def callback_model_states(self):
    #     pass

    def use_sim_time(self):
        rospy.set_param('/use_sim_time', True)

    def pause(self):
        """
            Function to Reset the Simulator
        """
        rospy.loginfo("Pausinig Simulation")
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/pause_physics', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def unpause(self):
        """
            Function to Reset the Simulator
        """
        rospy.loginfo("Resuming Simulation")
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/unpause_physics', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def reset(self):
        """
            Function to Reset the Simulator
        """
        rospy.loginfo("Resetting Simulation")
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/reset_simulation', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def reset_world(self):
        """
            Function to Reset the Simulator
        """
        rospy.loginfo("Resetting the world")
        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/reset_world', Empty)
            reset_serv()
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def set_moon_physics(self):
        """
        Set Physics to Moon
        """
        rospy.loginfo("Changing Gravity")
        serve = SetPhysicsProperties()
        ode_data = ODEPhysics()
        gravity = Vector3()

        gravity.x = 0.0
        gravity.y = 0.0
        gravity.z = -1.6

        ode_data.auto_disable_bodies = False
        ode_data.sor_pgs_precon_iters = 0
        ode_data.sor_pgs_iters = 0
        ode_data.sor_pgs_w = 0.0
        ode_data.sor_pgs_rms_error_tol = 0.0
        ode_data.contact_surface_layer = 0.0
        ode_data.contact_max_correcting_vel = 0.0
        ode_data.cfm = 0.0
        ode_data.erp = 0.0
        ode_data.max_contacts = 0

        serve.time_step = 1.0
        serve.max_update_rate = self.max_update_rate
        serve.gravity = gravity
        serve.ode_config = ode_data

        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/set_physics_properties', SetPhysicsProperties)
            reset_serv(serve.time_step, serve.max_update_rate, serve.gravity, serve.ode_config)
            rospy.loginfo("Moon's gravitational field activated.")
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))

    def set_earth_physics(self):
        """
        Set Physics to Earth
        """
        rospy.loginfo("Changing Gravity")
        serve = SetPhysicsProperties()
        ode_data = ODEPhysics()
        gravity = Vector3()

        gravity.x = 0.0
        gravity.y = 0.0
        gravity.z = -9.8

        ode_data.auto_disable_bodies = False
        ode_data.sor_pgs_precon_iters = 0
        ode_data.sor_pgs_iters = 0
        ode_data.sor_pgs_w = 0.0
        ode_data.sor_pgs_rms_error_tol = 0.0
        ode_data.contact_surface_layer = 0.0
        ode_data.contact_max_correcting_vel = 0.0
        ode_data.cfm = 0.0
        ode_data.erp = 0.0
        ode_data.max_contacts = 0

        serve.time_step = 1.0
        serve.max_update_rate = self.max_update_rate
        serve.gravity = gravity
        serve.ode_config = ode_data

        try:
            reset_serv = rospy.ServiceProxy('/lunar_world/set_physics_properties', SetPhysicsProperties)
            reset_serv(serve.time_step, serve.max_update_rate, serve.gravity, serve.ode_config)
            rospy.loginfo("Earth's gravitational field activated.")
        except rospy.ServiceException as e:
            rospy.loginfo("Service execution failed: %s" + str(e))


if __name__ == '__main__':
    try:
        sim = Gazebo()
    except KeyboardInterrupt:
        exit()
