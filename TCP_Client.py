#!/usr/bin/env python3

import socket

target_host = "0.0.0.0"
target_port = 9001

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the client
client.connect((target_host, target_port))

#Send some data
client.send(b"Hello There!")

#Receive some data
response = client.recv(4096)

print(response.decode())
client.close()
