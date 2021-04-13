#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 27/03/2021
# python-v  | 3.5.3
# -
# file      | overview.py
# project   | MonSy
# 
import modules.sov as sov
import os

# handle storing
def prepareStoring(self):
    pre_file = self.out_directory + "overview/system-overview.txt"
    
    if os.path.exists(pre_file):
        os.remove(pre_file)
    file = open(pre_file, "w")
    file.write("\nSYSTEM OVERVIEW - created by Mon(t)Sy\n")
    file.write("\nMon(t)Sy Software - developed by ZyzonixDev | published by ZyzonixDevelopments in 2021\n")
    
    return file    


# retrieving modules; adding to dict
def retrieveModules(self):
    modules = {}
    fromConfig = self.enabled_module_list["s"]
    # getting all available functions 
    # access functions: modules[function]()
    all_keys = len(fromConfig.keys())
    counter = 1
    
    while counter <= all_keys:
        modules[fromConfig[counter]] = getattr(sov, fromConfig[counter])
        counter += 1
    
    return modules