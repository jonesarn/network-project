import os
import platform
def scan_network():
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
            parts = ip.split(".")
            for ip in ip_list:
                parts = ip.split(".")
        # delete last part of the addres so we can make a network address
        # Have to the add a zero then add that zro to our network address
    return ip_list 

def get_network_address(ip):
    parts = ip.split(".")
    parts.pop()
    parts.append("0")
    network_address =".".join(parts)
    print("Network Adress: ",network_address)
    return network_address

ips = scan_network()  
if ips:
    network = get_network_address(ips[0])   
    print(network)  
              




              


   
      
      

