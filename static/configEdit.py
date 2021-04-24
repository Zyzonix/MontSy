#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 18/03/2021
# python-v  | 3.5.3
# -
# file      | configEdit.py
# project   | MontSy (Setup)
# version   | 0.9.6
# 
from configparser import ConfigParser
import os
import grp
import pwd
# getting config file
conf = ConfigParser(comment_prefixes='/', allow_no_value=True)
configFile = "static/config.ini"
conf.read(configFile)

lvalue = input("Should the log be enabled? (y/n)\n")
if lvalue == "y":
    conf["CONFIGURATION"]["log_enabled"] = str(1)
else:
    conf["CONFIGURATION"]["log_enabled"] = str(0)

try:
    svalue = int(input("Which storge method do you prefer? (XLSX = 2, SQLite = 1, both = 0)\n"))
    conf["CONFIGURATION"]["mon_storage_method"] = str(svalue)
    dur = int(input("What should be the time between each monitoring cycle? (in seconds)\n"))
    conf["CONFIGURATION"]["log_dur"] = str(dur)
except:
    print("please enter a valid value (requires a restart: python3 configEdit.py)\n")

path = os.path.abspath(os.getcwd()).replace("MontSy", "MontSy_OUTPUT/")
print("output directory set to: " + path)
conf["CONFIGURATION"]["output_dest"] = path

# requesting user for execution
user = input("Which user will execute the main class? (Standard: pi)\n")
if user == "":
    user = "pi"
uid = pwd.getpwnam(user).pw_uid
gid = grp.getgrnam(user).gr_gid
conf["CONFIGURATION"]["user"] = user

if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path + "overview"):
    os.mkdir(path + "overview")
    os.chown(path + "overview", uid, gid)
if not os.path.exists(path + "monitoring"):
    os.mkdir(path + "monitoring")
    os.chown(path + "monitoring", uid, gid)

# writing data to conf-file    
with open(configFile, "w") as file:
    conf.write(file)
print("Config writing done")
