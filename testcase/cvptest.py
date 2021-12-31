import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.255.108.85", username="arista",password="arista", allow_agent=False)
stdin, stdout, stderr = ssh.exec_command("top -b -n 10 -d.2 | grep 'Cpu' |  awk 'NR==3{ print($2)}'")
#time.sleep(5)
out=stdout.readline()
print(out)
ssh.close