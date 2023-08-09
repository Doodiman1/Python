#!/usr/bin/env python3

import socket

HOST = '192.168.1.151' 

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sniffer.bind((HOST, 0))
