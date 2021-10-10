import socket, sys

hostname = str(sys.argv[1])

ip = socket.gethostbyname(hostname)

print(hostname +' has an IP of' + ip)