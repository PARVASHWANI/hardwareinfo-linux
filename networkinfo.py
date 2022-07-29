# importing the required modules
import psutil

# writing a function to convert the bytes into gigabytes
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# gathering all network interfaces (virtual and physical) from the system
if_addrs = psutil.net_if_addrs()

# printing the information of each network interfaces
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print("\n")
        print(f"Interface :", interface_name)
        if str(address.family) == 'AddressFamily.AF_INET':
            print("[+] IP Address :", address.address)
            print("[+] Netmask :", address.netmask)
            print("[+] Broadcast IP :", address.broadcast)
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print("[+] MAC Address :", address.address)
            print("[+] Netmask :", address.netmask)
            print("[+] Broadcast MAC :",address.broadcast)

# getting the read/write statistics of network since boot
print("\n")
net_io = psutil.net_io_counters()
print("[+] Total Bytes Sent :", bytes_to_GB(net_io.bytes_sent))
print("[+] Total Bytes Received :", bytes_to_GB(net_io.bytes_recv))
