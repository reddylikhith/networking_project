import socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('192.168.149.133',1347))
msg=sk.recv(1024)
print(msg.decode("utf-8"))