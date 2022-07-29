# importing the required libraries
import psutil

# function to convert bytes to Gigabytes
def bytes2gb(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# using vertual_memory() function to replace a tuple
virtual_memory = psutil.virtual_memory()

# printing primary memory details
print("[+] Total Memory present :", bytes2gb(virtual_memory.total), "GB")
print("[+] Total Memory available :", bytes2gb(virtual_memory.available), "GB")
print("[+] Total Memory Used :", bytes2gb(virtual_memory.used), "GB")
print("[+] Percentage Used :", virtual_memory.percent, "%")
print("\n")

# printing swap memory details if available
swap = psutil.swap_memory()
print(f"[+] Total Swap Memory : {bytes2gb(swap.total)}")
print(f"[+] Free Swap Memory : {bytes2gb(swap.free)}")
print(f"[+] Used Swap Memory : {bytes2gb(swap.used)}")
print(f"[+] Percantage Used : {swap.percent}%")

# gathering memory info from meminfo file
print("\nReading the /proc/meminfo file: \n")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("[+] " + lines[0].strip())
print("[+] " + lines[1].strip())
