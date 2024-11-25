# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("10", username="admin", password="123")
# _, stdout, _ = ssh.exec_command("echo 123| sudo -i")

import shlex
import subprocess
Username="ape"
HOST = "10.204.90.31"

# cmd  = "ssh {0}@{1} 'ifconfig'".format(Username, HOST)
# subprocess.call(shlex.split(cmd))

ssh = subprocess.Popen(["ssh", "%s" %HOST],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
# if result == []:
#     error = ssh.stderr.readlines()
#     # print >>sys.stderr, "ERROR: %s" % error
# else:
#     print(result)