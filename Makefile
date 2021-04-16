#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 13/04/2021
# type		| Makefile
# -
# file      | Makefile
# project   | MontSy
# 

# executing the setup
all: help

# setting up (ignore errors)
setup:
	make -i setup_i

# setting up (starting shell script)
setup_i:
	@echo "---------------------"
	@echo starting MontSy setup
	@echo started setup
	@echo "---------------------"
	sudo chmod +x static/setup.sh
	sudo chmod +x static/view_status.sh
	sudo ./static/setup.sh

# removing all entries / files / folders
uninstall:
	@echo ""
	@echo uninstalling MontSy
	@echo ""



# starting systemd-service
start:
	@echo uninstalling system service
	@echo
	sudo systemctl start montsy.service

# stopping systemd-service
stop:	
	@echo stopping system service
	@echo ""
	sudo systemctl stop montsy.service

# installing service
enable:
	@echo installing system service
	@echo ""
	sudo systemctl enable montsy.service

# uninstalling service
disable:
	@echo uninstalling system service
	@echo ""
	sudo systemctl disable montsy.service

status: check
# check status of service
check: 
	@echo "checking status"
	@echo ""
	@echo "the following error is due to the command - don't worry"
	@echo ""
	sudo ./static/view_status.sh

# printing all commands of this file
help:
	@echo ""
	@echo "------------------------- [MontSy - Installation - HELP] -------------------------"
	@echo "--> some commands must be run as ROOT (with root privilegs (sudo))"
	@echo ""
	@echo "- sudo make setup..................starts the setup script"
	@echo "- sudo make uninstall..............removes the software from this device"
	@echo "- sudo make start..................starts the system service"
	@echo "- sudo make stop...................stops the system service"
	@echo "- sudo make enable.................installs the system service"
	@echo "- sudo make disable................uninstalls the system service"
	@echo "- make check.......................shows the status of the MontSy system service"
	@echo "----------------------------------------------------------------------------------"
	@echo ""