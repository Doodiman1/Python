# PetCat

PetCat is a simple Python script that allows you to establish a reverse shell or execute commands on a target machine over a network connection.

## Features

- Command shell: Gain access to a command shell on the target machine.
- Execute command: Execute a specified command on the target machine.
- Upload file: Upload a file to the target machine.
- Listen mode: Set up the script to listen for incoming connections.
- Flexible usage: Connect to the target machine, send text data, and perform various operations.

## Usage

```shell
python3 PetCat.py [options]

Options

    -c, --command            : Start a command shell on the target machine.
    -e, --execute <COMMAND>  : Execute a specified command on the target machine.
    -l, --listen             : Set up the script to listen for incoming connections.
    -p, --port <PORT>        : Specify the port number to connect to or listen on (default: 9001).
    -t, --target <IP>        : Specify the target IP address (default: 192.168.1.10).
    -u, --upload <FILE>      : Upload a file to the target machine.
```


## Dependencies
    Python 3
    pyfiglet library


### Install the required library using the following command:
``` shell
pip install pyfiglet
```

## Disclaimer
This script is provided for educational and ethical purposes only. 
Any unauthorized use is the responsibility of the user. The author is not liable for any damages or illegal activities caused by using this script.
