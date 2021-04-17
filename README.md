# MontSy - The system monitoring tool

[![Version](https://img.shields.io/badge/Version-0.9.2%20(beta)%20-orange)]() 
[![Python-Version](https://img.shields.io/badge/Python-3.5.3-blue)]()
[![last updated](https://img.shields.io/badge/last%20update-15/04/2021-9cf)]()

The main purpose of this **Mont**(itoring)**Sy**(stem) software is monitoring system statistics, mainly of linux-based systems. The system can be configured in different ways, it's core application collects all data from the config file under static before each run. The software was mainly developed for linux-based system, especially for Raspberry Pi OS systems, but MontSy can still be run on all linux-based devices that support Python3.5 or higher. 

MontSy is based on different modules, which can be switched on and off individually. 
The main functions are the following:
- system monitoring - records all relevant system data (cpu-usage a.e.)
- system overview - creates a hardware system overview (cpu-type a.e.)

All official patch notes can be found within the description of each release or in the README of the patch-notes-branch.
(Doesn't affect on beta / dev-branch releases)

The dev-branch patch notes can be found in the README of the patch-notes-branch.


## Table of content
* [Requirements](#requirements)
* [Installation](#installation)
* [Controlling](#controlling)
  - [Software controlling](#software-controlling)
  - [Uninstallation](#uninstallation)
* [How MontSy works](#how-it-works)
* [About the project](#about-the-project)


## Requirements
MontSy can be run on all devices/operating systems, that support Python 3.5 or higher. It is also recommendable to execute it on linux-based systems. The auto-setup scripts (Shell/Bash) and Makefiles can only be executed if the system supports them. 

To install MontSy also Root permission (sudo) are required. But it is recommendable to run MontSy as an other user which is not the root user.

**Please notice that MontSy won't work on Windows/MacOS**

If you wish to monitor your system statistics on Windows contact the developer via email (zyzonix@gmail.com). In this case a manual setup is reqired.


## Installation
To install MontSy download the whole project via git to your device and enter the downloaded folder:
```
$ git clone https://github.com/Zyzonix/MontSy.git
$ cd MontSy/
```
Before you can start entering the setup, you have to insert the correct paths to the system service file. Proceed as shown below:
```
$ cd static
$ nano montsy.service
```
Now insert the correct paths of the software and python (if Python is not installed, the installer will do this for you, then you can leave everything until the first space, so how it is) in line 6 after ExecStart=. It is also required to enter a correct working directory in line 7. (Directory where the software will be executed)

Close the Nano-editor with **ctrl+x** and save the file through typing **Y + Enter**.


You can now decide if you wish to configure MontSy on your own or if you wish that the Makefile-installer does this for you.
To enter the autosetup type:
```
$ Make 
$ Make setup
```
The first command will show you the help menu of the Makefile, the second will start the autosetup.
The Make-installer will execute a shell-setup-script, that will do the following:
- checking if the correct python version is installed, if not it will install Python3
- installing all required Python packages
- copying the system service to its correct directory
- start a config-setup script (You just have to answer the questions at the end)

From now on MontSy is installed properly.


## Controlling
#### Software controlling:
Through the Makefile it is very easy to control MontSy.

- The Makefile help menu can be found by typing
```
$ Make 
```
- To start the system service type
```
$ Make start
```
- To stop the system service type
```
$ Make stop
```
- To enable the system service type (the MontSy software will automatically start after each boot)
```
$ Make stop
```
- To disable the system service type (the MontSy software will no longer start automatically after each boot)
```
$ Make stop
```
- To show the system service status type
```
$ Make status
```
- To enable specific monitoring and overview modules you have to edit the configfile manually. A script for this will come in a future release.

- To create a hardware overview and start the monitoring type
```
$ python3 core.py 
```
After exiting the window, the script will interrupt.


- If you wish to create a hardware overview type
```
$ python3 core.py s 
```
- If you wish to start the monitoring manually type (the script will interrupt when the session ends)
```
$ python3 core.py m 
```


#### Uninstallation:
- To uninstall MontSy from your device type (not available in release 0.9.1)
```
$ Make uninstall
```
The Makefile will do the rest for you.

## How it works
MontSy uses libaries as gputil and psutil to collect as much information about your device as possible. 
The monitoring module will run at a certain interval that can be changed through the setup or manually through editing the configfile in the static directory, the collected data can then be saved in a SQLite database or within an excel sheet.
The overview module collects its data and writes this data to a systemoverview.txt file, the output directory for both modules will be set by executing the Make setup.

## About the project
My number of Raspberry Pi's has increased through the coronavirus pandemic, additionally I wasn't sure if my Raspberry Pi that provides a VPN-router and a DNS system (pihole) can handle the increased data traffic through home office and home schooling. Therefore I needed a simple tool, that can monitor the system "health" so that I can see if it's necessary to change the device for my VPN-router or the DNS. Another reason for developing this tool was to see how all the other Pi's and NAS/router/accesspoint systems are performing.
