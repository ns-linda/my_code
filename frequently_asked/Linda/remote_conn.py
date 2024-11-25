import subprocess
import sys

Host = "10.204.90.31"
username  = "ape"
password = "Psecure123"

# connect = subprocess.Popen(['ssh', 'ape@10.204.90.31'], shell= True,
#                            stdout = subprocess.PIPE,
#                            stderr = subprocess.PIPE).communicate()
# result= connect.stdout.readlines()

# import paramiko
# ssh = paramiko.client.SSHClient()
# ssh.load_system_host_keys()
# # ssh.load_host_keys('~/.ssh/known_hosts')
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect(Host, username=username, password=password, look_for_keys=False)
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("pwd")
# import shlex
# cmd = "ssh {0}@{1} 'pwd; ls -ltrh'".format(username,Host)
# subprocess.call(shlex.split(cmd))

import shlex
cmd = "ssh {0}@{1} 'ifconfig;'".format(username, Host)
subprocess.call(shlex.split(cmd))

import shlex
cmd = "ssh {0}@{1} 'ipconfig; pwd'". format(username,Host)
subprocess.call(shlex.split(cmd))

