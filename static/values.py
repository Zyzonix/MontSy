#!/usr/bin/python3
# 
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 27/03/2021
# python-v  | 3.5.3
# -
# file      | values.py
# project   | MontSy
# -

# static entries/values for module handling and other stuff
module_dictionary = {
    "mon" : [],
    "sov" : []
}
mon = {
    "console" : "creating system overview",
    "config" : "MODULES-TO-MON",
    "m" : "mon"
}
sov = {
    "console" : "starting system monitoring",
    "config" : "MODULES-TO-SOV",
    "s" : "sov"
}
static = {
    "all" : {"all" : "creating system overview (sov) and starting system monitoring (mon)"},
    # belongs to SYSTEM OVERVIEW
    "s" : sov,
    # belongs to MONITORING
    "m" : mon
}
sov_headers = {
    "system_info" : "\n\n" + "~"*20 + " GENERAL SYSTEM INFO " + "~"*20,
    "cpu_info" : "\n\n" + "~"*20 + " PROCESSOR INFO " + "~"*20,
    "gpu_info" : "\n\n" + "~"*20 + " GRAPHIC PROCESSOR INFO " + "~"*20,
    "ram_info" : "\n\n" + "~"*20 + " MEMORY INFO " + "~"*20,
    "disk_info" : "\n\n" + "~"*20 + " DISK(S) INFO " + "~"*20,
    "boot_info" : "\n\n" + "~"*20 + " BOOT INFO " + "~"*20,
    "user_info" : "\n\n" + "~"*20 + " USER INFO " + "~"*20,
    "network_info" : "\n\n" + "~"*20 + "NETWORK INFO " + "~"*20
}
mon_headers = {

}
module_headers = {
    "mon" : mon_headers,
    "sov" : sov_headers
}
class colorsetting:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

storageMethod = {
    0 : [".db", ".xlsx"],
    1 : [".db"],
    2 : [".xlsx"]
}
tables_names = {
    "networkmonitoring" : "Network",
    "generalmonitoring" : "General"
}
table_content = {
    "networkmonitoring" : "",
    "generalmonitoring" : ""
}
