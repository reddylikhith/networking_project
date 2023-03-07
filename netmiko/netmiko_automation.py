from netmiko import ConnectHandler
deviec={
    "device_type":"cisco_ios",
    "ip":"10.10.20.48",
    "username":"developer",
    "password":"C1sco12345"
}
connection=ConnectHandler(**deviec)
cpu_output=connection.send_command("show processes cpu")
mem_output=connection.send_command("show memory statistics")
connection.disconnect()
print("CPU Information:")
print(cpu_output)
print("\nMemory Information:")
print(mem_output)