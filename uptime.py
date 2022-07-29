from datetime import datetime
import psutil

# using psutil library to get boot time of the system
boot_time = datetime.fromtimestamp(psutil.boot_time())
print("[+] System Boot Time :",boot_time) 

# getting thesystem up time from the uptime file at proc dir
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()

uptime = int(float(uptime))
uptime_hrs = uptime // 3600
uptime_min = (uptime % 3600)//60
print("[+] System Uptime : " + str(uptime_hrs) + ":" + str(uptime_min) + " hours")
