import pytest
#from LoginFun.LoginDevice import LoginSSH
import paramiko
from utilities.CustomeLogger import LogGen
from utilities.ReadProperties import ReadConfig
import time
import sys
class Test_CPU:
    
    logger=LogGen.loggen()
    def test_ssh(self,setup_ssh):
        self.logger.info("************Test_SSH*************")
        self.ssh=setup_ssh
        self.logger.info("************Test_SSH Connection Start*************")
        try:
            stdind, stdoutd, stderrd = self.ssh.exec_command("whoami")
            #out1=out[0]
            out_d=stdoutd.read().decode().splitlines()
        except paramiko.SSHException as e:
            print("exception", str(e))
            sys.exit(-1)
        self.logger.info("************Test_SSH Connection Output Collected*************")
        self.ssh.close
        print("user name is ",out_d)
        if out_d[0]=="mahesh":
            self.logger.info("************Test_SSH Connection Output matched*************")
            assert True==True
        else: 
            self.logger.info("************Test_SSH Connection Output not matched*************")
            True==False
    def testssh_cpu(self,setup_ssh):
        
        self.logger.info("************Test_SSH CPU start*************")
        self.ssh=setup_ssh
        try:
            stdind, stdoutc, stderrd = self.ssh.exec_command("top -b -n 10 -d.2 | grep 'Cpu' |  awk 'NR==3{ print($2)}'")
            #out1=out[0]
            out_cpu=stdoutc.readline()
            time.sleep(2)
        except paramiko.SSHException as e:
            print("exception", str(e))
            sys.exit(-1)
        self.logger.info("************Test_SSH CPU Output Collected*************")
        self.ssh.close
        print("cpu utilization ",int(out_cpu[0]))
        if int(out_cpu[0])<90:
            self.logger.info("************Test_SSH CPU Output below Threshold*************")
            assert True==True
        else:
            self.logger.info("************Test_SSH CPU Output above Threshold*************")
            assert True==False

    def testssh_mem(self,setup_ssh):
        
        self.logger.info("************Test_SSH Memory start*************")
        self.ssh=setup_ssh
        try:
            stdind, stdoutm, stderrd = self.ssh.exec_command("awk \'/^Mem/ {printf(\"%u%%\", 100*$3/$2);}\' <(free -m)")
            #out1=out[0]
            out_mem=stdoutm.readline()
            time.sleep(2)
        except paramiko.SSHException as e:
            print("exception", str(e))
            sys.exit(-1)
        self.logger.info("************Test_SSH Memory Output Collected*************")
        self.ssh.close
        print("Memory utilization ",int(out_mem[0]))
        if int(out_mem[0])<90:
            self.logger.info("************Test_SSH Memory Output below Threshold*************")
            assert True==True
        else:
            self.logger.info("************Test_SSH Memory Output above Threshold*************")
            assert True==False
    def testssh_disk(self,setup_ssh):
        
        self.logger.info("************Test_SSH Disk start*************")
        self.ssh=setup_ssh
        try:
            stdind, stdoutd, stderrd = self.ssh.exec_command("df --output=pcent")
            #out1=out[0]
            out_disk=stdoutd.read().decode().splitlines()
        except paramiko.SSHException as e:
            print("exception", str(e))
            sys.exit(-1)
        out_disk.remove(out_disk[0])
        self.logger.info("************Test_SSH Disk Output Collected*************")
        self.ssh.close
        disk_list=[]
        for line in out_disk:
            #print(line[1:3])
            disk_list.append(int(line[0:3]))
        disk_list.sort()
        print("highest disk utilization ",disk_list[-1])
        if disk_list[-1]<90:
            self.logger.info("************Test_SSH Memory Output below Threshold*************")
            assert True==True
        else:
            self.logger.info("************Test_SSH Memory Output above Threshold*************")
            assert True==False
    
        

