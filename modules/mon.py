#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 21/03/2021
# python-v  | 3.5.3
# -
# file      | mon.py
# project   | MontSy
# project-v | 0.9.6
# 
import psutil
import os
from datetime import datetime
from static.values import colorsetting as color

# time service
def getTime():
    curTime = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    return curTime

def make_readable(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return "'" + str(bytes) + " " + unit + suffix + "'"
        bytes /= factor

# Structure:
# dict[name=values](dict[name=number](value_type))
#
# INFO for GitHub: NETWORK: all localhost information wont be listed

# cpu freq in MHz
def cpu_utilisation():
    try:
        value = {}
        value[1] = {"cpu_freq_current" : float(psutil.cpu_freq().current)}
        value[2] = {"cpu_freq_total" : float(psutil.cpu_freq().max)}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting CPU_UTILISATION" + color.END)    
        return {}

def cpu_percent():
    try:
        value = {}
        value[1] = {"cpu_freq_percent" : float(psutil.cpu_percent(interval=0.5))}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting CPU_PERCENT" + color.END)    
        return {} 

def cpu_running_processes():
    try:
        pids = []
        value = {}
        try:
            for subdir in os.listdir("/proc"):
                if subdir.isdigit():
                    pids.append(subdir)    
            value[1] = {"cpu_running_pids" : float(len(pids))}
        except:
            print(getTime(), "something went wrong -  was not able to collect currently running processes")            
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting CPU_RUNNING_PROCESSES" + color.END)    
        return {}  

def virtual_memory_percent():
    try:
        value = {}
        value[1] = {"ram_percent" : float(psutil.virtual_memory().percent)}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting VIRTUAL_MEMORY_PERCENT" + color.END)    
        return {}  


def virtual_memory_utilisation():
    try:
        value = {}
        value[1] = {"ram_currently_used" : float((psutil.virtual_memory().total - psutil.virtual_memory().available))/1024/1024}
        value[2] = {"ram_total" : float(psutil.virtual_memory().total)/1024/1024}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting VIRTUAL_MEMORY_UTILISATION" + color.END)    
        return {}  


def swap_ram_utilisation():
    try:
        value = {}
        value[1] = {"swap_currently_used" : float(psutil.swap_memory().used)/1024/1024}
        value[2] = {"swap_total" : float(psutil.swap_memory().total)/1024/1024}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting SWAP_RAM_UTILISATION" + color.END)    
        return {}  


def swap_ram_percent():
    try:
        value = {}
        value[1] = {"swap_percent" : float(psutil.swap_memory().percent)}
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting SWAP_RAM_PERCENT" + color.END)    
        return {}  


def net_io_counters():
    try:
        value = {}
        alldata = psutil.net_io_counters(pernic=True)
        ifaces = alldata.keys()
        value_list = 1
        for key in ifaces:
            if not key == "lo":
                value[0 + value_list] = {key + "_bytes_sent" : float(alldata[key].bytes_sent)}
                value[1 + value_list] = {key + "_bytes_received" : float(alldata[key].bytes_recv)}
                value[2 + value_list] = {key + "_packets_sent" : float(alldata[key].packets_sent)}
                value[3 + value_list] = {key + "_packets_received" : float(alldata[key].packets_recv)}
                value_list += 4
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting NET_IO_COUNTERS" + color.END)    
        return {}  


def net_connections():
    try:
        value = {}
        alldata = psutil.net_connections()
        value_counter = 1
        local_ip_port_list = {}
        remote_ip_port_list = {}
        iface_counter = 1
        for item in alldata:
            ip_data = item.laddr.ip
            if not (ip_data.startswith(":") or ip_data.startswith("127") or ip_data.startswith("0")):
                local_ip_port_list[ip_data] = str(item.laddr.port)
            try:  
                rip_data = item.raddr.ip
                if not (rip_data.startswith(":") or rip_data.startswith("127") or rip_data.startswith("0")):
                    remote_ip_port_list[rip_data] = str(item.raddr.port)
            except Exception as e:
                pass
        for key in list(local_ip_port_list.keys()):
            value[0 + value_counter] = {type(item).__name__ + str(iface_counter) + "_local_address_ip_port" : key + "_" + local_ip_port_list[key]}
            value_counter += 1
            iface_counter += 1
        for key in list(remote_ip_port_list.keys()):
            value[0 + value_counter] = {type(item).__name__ + str(iface_counter) + "_local_address_ip_port" : key + "_" + remote_ip_port_list[key]}
            value_counter += 1
            iface_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting NET_CONNECTIONS" + color.END)    
        return {}  


def net_if_addrs():
    try:
        value = {}
        data = psutil.net_if_addrs()
        value_counter = 1
        iface_counter = 1
        for iface in data:
            data_values = data[iface]
            if not iface.startswith("lo"):
                for item in data_values:
                    value[0 + value_counter] = {iface + "_ip_address_" + str(iface_counter) : item.address}
                    value[1 + value_counter] = {iface + "_netmask_" + str(iface_counter) : item.netmask}
                    value_counter += 2
                    iface_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting NET_IF_ADDRS" + color.END)    
        return {}  


# usage in percent
def disk_usage():
    try:
        value = {}
        disk_info = psutil.disk_partitions()
        mp_list = {}
        for disk in disk_info:
            mp_list[disk.device] = disk.mountpoint
        value_counter = 1
        for mp in mp_list.keys():
            value[0 + value_counter] = {"'" + mp + "_percent'" : float(psutil.disk_usage(mp_list[mp]).percent)}
            value_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting DISK_USAGE" + color.END)    
        return {}  


# used space 
def disk_utilisation():
    try:
        value = {}
        disk_info = psutil.disk_partitions()
        mp_list = {}
        for disk in disk_info:
            mp_list[disk.device] = disk.mountpoint
        value_counter = 1
        for mp in mp_list.keys():
            value[0 + value_counter] = {"'" + mp + "'" : make_readable(psutil.disk_usage(mp_list[mp]).used)}
            value_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting DISK_UTILISATION" + color.END)    
        return {}  


# THE FOLLOWING PART WILL BE DEVELOPED IN A FURTHER VERSION
# only NVIDIDA GPU's
def gpu_percent():
    print("")

def gpu_freq():
    print("")

def gpu_temp():
    print("")

def gpu_vram_percent():
    print("")

def gpu_vram_utilisation():
    print("")
# UNTIL HERE

def sensors_temperatures():
    try:
        value = {}
        temp_info = psutil.sensors_temperatures()
        value_counter = 1
        for temp in temp_info:
            for content in temp_info[temp]:
                try:
                    rew_temp = temp.replace("-", "_")
                except Exception as e:
                    print(e)
                    rew_temp = temp
                value[0 + value_counter] = {rew_temp : float(content.current)}
            value_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting SENSORS_TEMPERATURES" + color.END)    
        return {}  


def sensors_fan():
    try:
        value = {}
        fan_info = psutil.sensors_fans()
        value_counter = 1
        for fan in fan_info:
            for content in fan_info[fan]:
                value[0 + value_counter] = {fan : float(content.current)}
            value_counter += 1
        return value
    except Exception as e:
        print(getTime(), color.RED + "something went wrong while collecting SENSORS_FAN" + color.END)    
        return {}  
