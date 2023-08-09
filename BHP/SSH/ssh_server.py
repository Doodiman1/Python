#!/usr/bin/env python3

import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename = os.path.join(CWD, "rsa_test.key"))

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

        def check_channel_request(self, kind, chanid):
            if kind == "session":
                return paramiko.OPEN_SUCCEEDED
            return paramiko.OPEN_FAILED_ADINISTRATIVELY_PROHIBITED

        def check_auth_password(self, username, password):
            if (username == "perry") and (password == "hello"):
                return paramiko.AUTH_SUCCESSFUL
            return paramiko.AUTH_FAILED

if __name__ == "__main__":
    server = "192.168.1.2"
    ssh_port = 22
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, +1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print("[+] Listening for Connection...")
        client, addr = sock.accept()
    except Exception as e:
        print("[-] Listening failed " + str(e))
        sys.exit
    else:
        print("[+] Got a Connection!", client, addr)

    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)
    server=Server()
    bhSession.start_server(server=server)

    chan = bhSession.accept(20)
    if chan is None:
        print("*** No Channel :(")
        sys.exit

    print("[+] Authenticated :)")
    print(chan.recv(1024))
    chan.send("Welcome to bh_ssh")
    try:
        while True:
            command = input("Enter command: ")
            if command != "exit":
                chan.send(command)
                r = chan.rev(8192)
                print(r.decode())
            else:
                chan.send("exit")
                print("exiting")
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()
