import os
import platform
import subprocess

def scan_network():
    network_bases = "192.168.1.","10.0.0.","176.16.1."
    ip_list = []
    
    if platform.system() == "Windows":
        ping_command = "-n"
    else:
        ping_command = "-c"
# Notes: We are leaving that blank so we can find multiple devices on this private IP
    for base in network_bases:
        for i in range(1,255):
            ip = base + str(i)

# Doing this as we learning python
        response = subprocess.run(
            ["ping",ping_command,"1",ip],
            capture_output = True,
            text= True
            )
      
        if response.returncode == 0 :
       # print(ip_list ,"is reachable")
            ip_list.append(ip)
            print(ip," are reachable")
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
## Now lets add our mac address
   
def get_mac_address(ip_list):
    arp_output = subprocess.getoutput("arp -a")
    lines = arp_output.split("\n")

    ip_mac ={}

    for line in lines:
        for ip in ip_list:
            if f"({ip})" in line:
                parts = line.split()
                mac = parts[3]
                ip_mac[ip]= mac
        return ip_mac
    

## How this runs is I call unto scan network. This scan network allows you to see every IP address availaible in my private etwork
### I then use that to show my network address. They should all be the same so it list every device then shows the network address
ips = scan_network()  
if ips:
    network = get_network_address(ips[0])   
    print(network)

macs = get_mac_address(ips)
print(macs)  
     





              


   
      
      

