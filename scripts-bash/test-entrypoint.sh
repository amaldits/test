#!/bin/bash

source /opt/ros/noetic/setup.bash
source /home/
TURTLEBOT3_MODEL=waffle
export SVGA_VGPU10=0

roslaunch test all.launch