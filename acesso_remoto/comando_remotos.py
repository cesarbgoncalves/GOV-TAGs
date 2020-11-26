import paramiko
address = 'zabbix'
username = 'cgoncalves'


def ssh_connect(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=username)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    return result


check_status = ssh_connect('systemctl status zabbix-server.service')

for line in check_status:
    print(line.replace('\n', ''))