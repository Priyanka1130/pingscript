import os
import subprocess   
server_name=['localhost']
for server in server_name:
    response = os.popen(" ping {server_name}").read()
    if "Recieved =1" in response:
        print( "\u001b[32m  UP {server_name} ping successful")
    else:
        print("\u001b[31m DOWN {server_name} ping unsuccessful")
