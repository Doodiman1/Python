#!/usr/bin/env python3

import paramiko as p

def ssh_command(ip, port, user, passwd, cmd):
    client = p.SSHClient()
    client.set_missing_host_key_policy(p.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _,stdout,stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print("----Output----")
        for line in output:
            print(line.strip())

if __name__ == "__main__":
    import getpass
    # user = getpass.getuser()
    user = input("Username: ")
    password = getpass.getpass()

    ip = input("Server IP: ") or "192.168.1.203"
    port = input("Enter Port or <CR>: ") or 2022
    cmd = input("Enter command or <CR>: ") or "id"
    ssh_command(ip, port, user, password, cmd)
