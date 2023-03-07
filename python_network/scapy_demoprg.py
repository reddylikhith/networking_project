from scapy.all import *
def demo(packet):
    print(packet.show())
sniff(iface='eth0',prn=demo,count=10)
