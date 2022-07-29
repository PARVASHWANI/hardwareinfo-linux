# importing the required packages
import psutil

# print the no. of CPU cores present
print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
print("\n")
# printing the max, min and current CPU frequency
cpu_frequency = psutil.cpu_freq()
print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
print(f"[+] Current Frequency : {cpu_frequency.current:.2f}Mhz")
print("\n")
# printing the CPU usage per core
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"[+] CPU Usage of Core {i} : {percentage}%")
print(f"[+] Total CPU Usage : {psutil.cpu_percent()}%")
print("\n")
# reading the cpuinfo file to print the name of the CPU present 
with open("/proc/cpuinfo", "r") as f:
    file_info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in file_info if "model name" in x]
for index, item in enumerate(cpuinfo):
    print("[+] Processor "+str(index)+ " : " + item)
