#!/usr/bin/env python3

import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
from pyfiglet import Figlet

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return 
    output = subprocess.check_output(shlex.split(cmd),
            stderr=subprocess.STDOUT)
    return output.decode()

class PetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())

        except KeyboardInterrupt:
                print("\nUser Terminated")
                self.socket.close()
                sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print("[+]Listening...") 
        while True:
            client_socket, _= self.socket.accept()
            client_thread = threading.Thread(
                    target=self.handle, args=(client_socket,)
                    )
            client_thread.start()


    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'PetCat: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server Killed {e}')
                    self.socket.close()
                    sys.exit()


if __name__ == "__main__":
    f = Figlet(font='slant')
    banner = f.renderText('PetCat!')
    

    parser = argparse.ArgumentParser(
        usage = f"%(prog)s [options]",
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = textwrap.dedent(''' Example:
            PetCat.py -t 192.168.1.10 -p 9001 -l -c                     # generate command shell
            PetCat.py -t 192.168.1.10 -p 9001 -l -u=mytest.txt          # upload to file
            PetCat.py -t 192.168.1.10 -p 9001 -l -e=\"cat /etc/passwd\"   # execute command
            echo 'ABC' | ./Petcat.py -t 192.168.1.10 -p 135             # echo text to server port 135
            PetCat.py -t 192.168.1.10 -p 9001                           # connect to server
            '''))

    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', metavar='COMMAND', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=9001, help='port number')
    parser.add_argument('-t', '--target', default='192.168.1.10', help='target IP')
    parser.add_argument('-u', '--upload', metavar='FILE', help='upload file')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        print(banner)
        parser.print_help()
        sys.exit()
    elif args.listen:
            buffer = ''
    else:
        buffer = sys.stdin.read()
    
    pc = PetCat(args, buffer.encode())
    pc.run()
