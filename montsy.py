#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 18/03/2021
# python-v  | 3.5.3
# -
# file      | montsy.py
# project   | MontSy
# project-v | 0.9.6
# 

# this file allows smooth loading of MontSy
from datetime import datetime
import sys
import threading
import time 
import itertools

# loading animation
def loadingAnimation():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        # checking if import is finished
        if loaded:
            # cancels for loop
            break
        sys.stdout.write('\r[' + str(datetime.now().strftime("%H:%M:%S")) + '] loading libraries ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# import finished indicator
loaded = False
print("\n[" + str(datetime.now().strftime("%H:%M:%S")) + "] running " + "\033[91m" + '\033[1m' +  "MontSy" + '\033[0m' + " (system monitoring and overview) application \n")
# starting loading animation
thread = threading.Thread(target=loadingAnimation)
thread.start()
# importing core
from core import Core
loaded = True
# updating loaded-var in thread
thread.join()
# executing the core
Core()    