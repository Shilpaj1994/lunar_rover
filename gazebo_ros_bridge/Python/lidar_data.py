#!/usr/bin/env python3.8
"""
Code for accessing lidar data from Gazebo and publish it on ROS topic
Author: Shilpaj Bhalerao
Date: Oct 16, 2020
"""

import sys
from trollius import From
import pygazebo.msg.laserscan_stamped_pb2 as scan


def callback(data):
    message = scan(data)
    print('Received message:', message.data)


def main():
    manager = yield From(pygazebo.connect(('localhost', 11345)))

    manager.subscribe('/gazebo/default/hokuyo/link/laser/scan',
                      'gazebo.msgs.LaserScanStamped',
                      callback)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        sys.exit()
        




