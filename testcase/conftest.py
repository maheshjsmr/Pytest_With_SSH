import pytest
import paramiko
from utilities.ReadProperties import ReadConfig
@pytest.fixture()
def setup_ssh():
    IP=ReadConfig.getipAddress()
    usern=ReadConfig.getUserName()
    passw=ReadConfig.getUserPass()
    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=IP, username=usern,password=passw, allow_agent=False)
    except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as e:
        print(str(e))

    return ssh
        