# importing required modules
import psutil

# accessing all the disk partitions
disk_part = psutil.disk_partitions()

# writing a function to convert bytes to Giga bytes
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# displaying the partition and usage information
for partition in disk_part:
    print("[+] Partition Device : ", partition.device)
    print("[+] File System : ", partition.fstype)
    print("[+] Mountpoint : ", partition.mountpoint)
    
    disk_usage = psutil.disk_usage(partition.mountpoint)
    print("[+] Total Disk Space :", bytes_to_GB(disk_usage.total), "GB")
    print("[+] Free Disk Space :", bytes_to_GB(disk_usage.free), "GB")
    print("[+] Used Disk Space :", bytes_to_GB(disk_usage.used), "GB")
    print("[+] Percentage Used :", disk_usage.percent, "%")

# get read/write statistics since boot
disk_rw = psutil.disk_io_counters()
print(f"[+] Total Read since boot : {bytes_to_GB(disk_rw.read_bytes)} GB")
print(f"[+] Total Write sice boot : {bytes_to_GB(disk_rw.write_bytes)} GB")
