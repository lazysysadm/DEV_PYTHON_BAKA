#!/bin/python3.6

#this script check status of process with systemctl
# when service is active, all is ok

##MODULES
import sys
import os
import subprocess

#when service is active, all is OK
OK=0
#when service is inactive
WARNING=1
#when a service is inactive
CRITICAL=2
# Other : service not exist, not found, error in servicename
UNKNOWN=3

#Check args
#Info obliged to use minus one beacause [0] is the relative path of script count 1 arg. So to no count it need to minus 1 to have 0 args. It's not like in bash.
numberAllArguments = int(len(sys.argv)) - 1
alertArgs = "Need process name"

# Check args
if numberAllArguments != 1:
   print(alertArgs)
   sys.exit(UNKNOWN)
else:
   proc = sys.argv[1]
   print("Process To check :", str(proc))

#check if service is on
cmd = ["systemctl", "status", "is active", proc]
launch_cmd = subprocess.run(cmd, stderr=subprocess.PIPE)
#print(launch_cmd)
print ("le code retour est:", launch_cmd.returncode)
print("----------")

if launch_cmd.returncode != OK:
   print(proc, "not found")
   sys.exit(UNKNOWN)