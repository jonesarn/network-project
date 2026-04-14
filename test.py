import os
response = os.system("ping -c 1 8.8.8.8")
if response == 0:
    print("Device is reachable")
else:
    print("Device isn't reachable")