#!/bin/bash
# Filename 	: setupZSH.sh
# Description	: 安装 Oh-my-zsh
# Author	: ihainan
# Created Date	: 2013/04/06
# E-mail	: ihainan72@gmail.com
# Website 	: http://www.ihainan.me

sudo apt-get install zsh
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.zshrc ~/.zshrc.orig
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s /bin/zsh
