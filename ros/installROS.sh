#!/bin/bash
# Filename 	: installROS.sh
# Description	: 安装 ros
# Author	: ihainan
# Created Date	: 2013/04/06
# E-mail	: ihainan72@gmail.com
# Website 	: http://www.ihainan.me

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu raring main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install ros-hydro-desktop-full
echo "source /opt/ros/hydro/setup.zsh" >> ~/.zshrc
source ~/.zshrc
sudo apt-get install python-rosinstall
sudo rosdep init
rosdep update
