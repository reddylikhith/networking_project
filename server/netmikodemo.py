from netmiko import ConnectHandler
device={
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "username" : "developer",
    "password":"C1sco@12345"
}
connection=ConnectHandler(**device)
print(connection)
output=connection.send_command("show interfaces")
print(output)
