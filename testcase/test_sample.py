import paramiko
import io
import datetime
import sys
import time
import pytest

def testread_cpu():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="3.110.90.193", username="mahesh",password="Maxkhatri94@", allow_agent=False)
    except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as e:
        print(str(e))
        sys.exit(-1)
    try:
        stdin, stdout, stderr = ssh.exec_command("top -b -n 10 -d.2 | grep 'Cpu' |  awk 'NR==3{ print($2)}'")
        #time.sleep(5)
        out=stdout.readline()
        time.sleep(2)
        
        
    except paramiko.SSHException as e:
        print("exception", str(e))
        sys.exit(-1)
    ssh.close
    
    
    print("cpu utilization ",int(out[0]))
    if int(out[0])<90:
        print("cpu threshold below 90")
        assert True==True
    else:
        print("cpu threshold above 90")
        assert True==False
    
    
def testread_memory():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="3.110.90.193", username="mahesh",password="Maxkhatri94@", allow_agent=False)
    except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as e:
        print(str(e))
        sys.exit(-1)
    try:
        cmd_m="awk \'/^Mem/ {printf(\"%u%%\", 100*$3/$2);}\' <(free -m)"
        stdinm, stdoutm, stderrm = ssh.exec_command(cmd_m)
        #out1=out[0]
        out_m=stdoutm.readline()
    except paramiko.SSHException as e:
        print("exception", str(e))
        sys.exit(-1)
    ssh.close
    print("memory utilization ",out_m[0])
    if int(out_m[0])<90:
        print("memory threshold below 90")
        assert True==True
    else:
        print("memory threshold above 90")
        assert True==False
def testread_disk():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="3.110.90.193", username="mahesh",password="Maxkhatri94@", allow_agent=False)
    except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as e:
        print(str(e))
        sys.exit(-1)
    try:
        stdind, stdoutd, stderrd = ssh.exec_command("df --output=pcent")
        #out1=out[0]
        out_d=stdoutd.read().decode().splitlines()
    except paramiko.SSHException as e:
        print("exception", str(e))
        sys.exit(-1)
    ssh.close
    out_d.remove(out_d[0])
    
    disk_list=[]
    for line in out_d:
        #print(line[1:3])
        disk_list.append(int(line[0:3]))
    disk_list.sort()
    
    print("highest disk utilization ",disk_list[-1])
    if disk_list[-1]<90:
        print("disk threshold below 90")
        assert True==True
    else:
        print("disk threshold above 90")
        assert True==False

        
    