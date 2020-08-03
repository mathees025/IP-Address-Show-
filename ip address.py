import socket
hostname = socket.gethostname()
IpAddr = socket.gethostbyname(hostname)
print("Ip Address is:" + IpAddr)
 
