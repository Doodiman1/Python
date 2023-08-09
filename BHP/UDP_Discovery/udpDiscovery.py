#!/usr/bin/env python3

import socket
import os

HOST = '192.168.0.15'

def main():
    socket_protocol = socket.IPPROTO_IP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket_protocol)
    sniffer.bind((HOST, 0))

    sniffer.setsockopt(socket.IPPROTO_RAW, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(sniffer.recvfrom(65565))

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()
