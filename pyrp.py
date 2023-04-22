import socket

mbuff = 2048
tarserver = "target.host.local"
tarip = "192.168.10.233"
tarport = 1433
linterface = "127.0.0.1"

def receiver(socket):
    message = socket.recv(mbuff)
    return message

def replacer(message):
    seek = b"""Vulnerable Packet"""
    payload = b"""commence hacking"""
    # This pbuff calc makes the assumption that message and payload are bytes objects
    pbuff = len(message) - len(payload)
    assembled = payload + b"""\x00""" * pbuff
    if seek in message:
        replaced = message.replace(seek,assembled)
        return replaced
    else:
        return message

def handler(vconn,tsock):
    while True:
        vmessage = receiver(vconn)
        payload = replacer(vmessage)
        tsock.sendall(payload)
        tmessage = receiver(tsock)
        vconn.sendall(tmessage)

vsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
vsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tsock.connect((tarip,tarport))
vsock.bind((linterface,tarport))
vsock.listen(5)
vconn,addr = vsock.accept()

handler(vconn,tsock)
