#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 21/03/2021
# python-v  | 3.5.3
# -
# file      | sov.py
# project   | MontSy
# project-v | 0.9.6
# 
import platform
import psutil
import cpuinfo 
import GPUtil
import pwd
from datetime import datetime
from static.values import colorsetting as color

# KEY's where the value is empty will be removed from the entry list

def getTime():
    curTime = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    return curTime

def make_readable(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return str(bytes) + " " + unit + suffix
        bytes /= factor

def system_info():
    try:
        info = []
        sysinfo = platform.uname()
        info.append({"System:\t\t\t" : sysinfo.system})
        info.append({"Hostname:\t\t" : sysinfo.node})
        info.append({"Release:\t\t" : platform.release()})
        info.append({"Platform:\t\t" : platform.platform()})
        info.append({"Architecture:\t" : sysinfo.machine + " | " + platform.architecture()[0]})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting SYSTEM_INFO" + color.END)    
        return []  

def cpu_info():
    try:
        info = []
        sysinfo = platform.uname()
        cpuinf = cpuinfo.get_cpu_info()
        info.append({"Processor:\t\t\t" : sysinfo.processor})
        info.append({"Processor brand:\t" : cpuinf["brand_raw"]})
        info.append({"Chip ID:\t\t\t" : cpuinf["hardware_raw"]})
        info.append({"Physical cores:\t\t" : psutil.cpu_count(logical=False)})
        info.append({"Total cores:\t\t" : psutil.cpu_count(logical=True)})
        info.append({"Max frequency:\t\t" : str(psutil.cpu_freq().max) + "(MHz)"})
        info.append({"Min frequency:\t\t" : str(psutil.cpu_freq().min) + "(MHz)"})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting CPU_INFO" + color.END)    
        return []  

    
def gpu_info():
    try:
        info = []
        av_gpus = GPUtil.getGPUs()
        gpu_numb = 1
        for gpu in av_gpus:
            if len(av_gpus) != 1:
                gpu_numb = gpu_numb
            else:
                gpu_numb = ""
            info.append({"GPU " + str(gpu_numb) + " ID:" : gpu.id})
            info.append({"GPU " + str(gpu_numb) + " model:" : gpu.name})
            info.append({"GPU " + str(gpu_numb) + " memory (MB):" : gpu.memoryTotal})
            if gpu_numb != "":
                gpu_numb = gpu_numb + 1
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting GPU_INFO" + color.END)    
        return []  


def ram_info():
    try:
        info = []
        info.append({"Total RAM:\t\t\t" : make_readable(psutil.virtual_memory().total)})
        info.append({"Total Swap RAM:\t\t" : make_readable(psutil.swap_memory().total)})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting RAM_INFO" + color.END)    
        return []  


def disk_info():
    try:
        info = []
        disk_inf = psutil.disk_partitions()
        info.append({"Diskpartition count:\t\t" : len(disk_inf)})
        disk_numb = 1 
        for disk in disk_inf:
            if len(disk_inf) != 1:
                disk_numb = disk_numb
            else:
                disk_numb = ""
            info.append({"Partition " + str(disk_numb) + " name:\t\t\t" : disk.device})
            info.append({"Partition " + str(disk_numb) + " mountpoint:\t\t" : disk.mountpoint})
            info.append({"Partition " + str(disk_numb) + " FS type:\t\t" : disk.fstype})
            try:
                d_usage = psutil.disk_usage(disk.mountpoint)
                info.append({"Partition " + str(disk_numb) + " total size:\t\t" : make_readable(d_usage.total)})
                info.append({"Partition " + str(disk_numb) + " space used:\t\t" : make_readable(d_usage.used)})
                info.append({"Partition " + str(disk_numb) + " space free:\t\t" : make_readable(d_usage.free) + "\n"})
            except:
                print(getTime(), "error while getting diskusage - skipping")
            if disk_numb != "":
                disk_numb = disk_numb + 1
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting DISK_INFO" + color.END)    
        return []  


def boot_info():
    try:
        info = []
        uptime = datetime.fromtimestamp(psutil.boot_time())
        info.append({"Boot time:\t" : str(uptime)})
        with open("/proc/uptime", "r") as f:
            rtime = f.read().split(" ")[0].strip()
        rtime = int(float(rtime))
        rtime_hours = rtime // 3600
        rtime_minutes = (rtime % 3600) // 60
        info.append({"Uptime:\t\t" : str(rtime_hours) + ":" + str(rtime_minutes) + "h | " + str(rtime) + " sec"})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting BOOT_INFO" + color.END)    
        return []  


def user_info():
    try:
        info = []
        users = pwd.getpwall()
        info.append({"User count:" : len(users)})
        for user in users:
            info.append({user.pw_name : "- home directory: \t" + user.pw_dir})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting USER_INFO" + color.END)    
        return []  


def network_info():
    try:
        info = []
        data = psutil.net_if_stats()
        for iface in list(data.keys()):
            content = data[iface]
            info.append({iface + " Network Speed:" : content.speed})
        return info
    except:
        print(getTime(), color.RED + "something went wrong while collecting NETWORK_INFO" + color.END)    
        return []  
    

# new data retrieve functions may be added in the future...