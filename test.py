import os
import platform
network_base = "192.168.1."
ip_list = []
if platform.system() == "Windows":
        ping_command = "-n 1"
else:
        ping_command = "-c 1"
# Notes: We are leaving that blank so we can find multiple devices on this private IP
for i in range(74,81):
    ip = network_base + str(i)
# Doing this as we learning python
    response = os.system(f"ping {ping_command} {ip}")
    if response == 0 :
       # print(ip_list ,"is reachable")
        ip_list.append(ip)
        print(ip_list," are reachable")

   

