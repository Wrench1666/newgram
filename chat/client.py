import socket

TCP_IP = "94.19.219.127"
TCP_PORT = 5800
BUFFER_SIZE = 1024
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((TCP_IP, TCP_PORT))
