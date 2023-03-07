import paramiko
import yaml
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
with open('datab.ymi','r') as f:
    config=yaml.safe_load(f)['database']
ssh.connect(hostname=config['hostname'],username=config['username'],password=config['password'])
#stdin,stdout,stderr=ssh.exec_command("pwd")
stdin,stdout,stderr=ssh.exec_command("ls -l")
#stdout=ssh.exec_command("pwd")
pr="permissions"
own="owner"
usr="user"
sz="size"
dt="date"
nm="name"
print("{0:8}{1:8}{2:8}{4:8}{5}".format(pr,own,usr,sz,dt,nm))
for f in stdout:
    print(f)
stdout.close()