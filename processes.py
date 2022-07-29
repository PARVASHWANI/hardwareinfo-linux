# importing OS library
import os
# iniatalizing process ID or PID variable
pid=[]
# Extraction of current running process and append in the list
for subdir in os.listdir('/proc'):
    if subdir.isdigit():
        pid.append(subdir)
# printing the total no. of processes
print('[+] Total number of processes : {0}'.format(len(pid)))
