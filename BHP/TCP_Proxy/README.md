# TCP Proxy

TCP Proxy is a Python script that acts as a network proxy, forwarding data between a local client and a remote server while providing the ability to modify packets before they are sent.

## Features

- Transparent proxying: Relays data between a local client and a remote server.
- Packet modification: Allows packet modification before sending and receiving.
- Hexadecimal dump: Provides a hexadecimal and printable representation of packet data.

## Usage

```shell
python3 TCP_Proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]

Arguments

    localhost		: The local host IP address.
    localport		: The local port to listen on.
    remotehost		: The remote server's IP address.
    remoteport		: The remote server's port.
    receive_first	: Set to True if you want to receive data from the remote server before relaying (default: False).
```
Example:
```shell
python3 TCP_Proxy.py 127.0.0.1 9001 10.12.132.1 9001 True
```

## Functionality

    Hexdump: The hexdump function converts packet data into a hexadecimal representation for analysis.

    Packet Handlers: The request_handler and response_handler functions can be customized to modify packets before sending and after receiving, respectively.

    Transparent Proxy: The proxy_handler function establishes connections between the local client and remote server, relaying data bidirectionally.
    
## Testing done with the following:

First Terminal:
```shell
sudo ./TCP_Proxy.py <LOCAL_IP> 21 ftp.gnu.org 21 True
```
Second Terminal:
```shell
ftp ftp.gnu.ord
	uname : anonymous
	passwd: none
```
## Disclaimer

This script is provided for educational and ethical purposes only. Any unauthorized use is the responsibility of the user. The author is not liable for any damages or illegal activities caused by using this script.
