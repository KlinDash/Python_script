
from paramiko import SSHClient, AutoAddPolicy 

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('192.168.2.100', userame='root', password='552081', port='221')
stdin, stdout, stderr = client.exec_command('hostname')
print(type(stdin))
print(type(stdout))
print(type(stderr))

print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stdout.read().decode("utf8")}')

stdin.close()
stdout.close()
stderr.close()

client.close()

