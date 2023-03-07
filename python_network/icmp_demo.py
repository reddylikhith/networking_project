from scapy.all import *
ip_address='192.168.149.133'
res=sr1(IP(dst=ip_address)/ICMP(),timeout=2)
if res is not None and res.haslayer(ICMP) and res[ICMP].flags==0:
	print(ip_address)
else:
	print('not found',ip_address)
