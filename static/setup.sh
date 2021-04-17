#!/bin/sh
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 13/04/2021
# python-v  | 3.5.3
# -
# file      | setup.sh
# project   | MontSy (Setup)
# 
echo -------------------
echo started SHELL setup
echo -------------------
echo Updating...
echo -------------------
sudo apt update
echo
# installing python3 (req: 3.5)
echo --------------------
echo Checking for python3
echo --------------------
sudo apt install python3
# checking if python packages are installes
echo
echo -------------------
echo installing packages
echo -------------------
pip install configparser
pip3 install openpyxl
pip3 install psutil
pip install GPUtil
pip3 install GPUtil
pip install py-cpuinfo

# pasting service into correct directory
echo
echo ---------------------------------------------
echo pasting system-service into correct directory
echo ---------------------------------------------
_cur_dir=$PWD
sudo cp $_cur_dir/static/montsy.service /lib/systemd/system/
echo done $_cur_dir/static/montsy.service copied

# showing status of system service
echo
echo ------------------------
echo Status of MontSy-Service
echo ------------------------
status=$(sudo systemctl status montsy.service)
echo $status

# changing owner of MontSy to root
echo
echo ----------------------------------
echo changing owner of MontSy-Directory
echo ----------------------------------
sudo chown root $_cur_dir

# setting up configurationpart of config.ini
echo
echo -----------------------------
echo setting parameters for MontSy
echo -----------------------------
/usr/bin/python3 static/configEdit.py

# confirming setup
echo
echo ---------------
echo Setup completed
echo ---------------