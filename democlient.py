import random
import socket
from time import sleep

#host = "target.host.local"
host = "127.0.0.1"
port = 1433
count = 1

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    payload1 = b"""\x00\x00\x00Innocent Packet\x00\x00\x00"""
    payload2 = b"""\x00\x00\x00Vulnerable Packet\x00\x00\x00"""
    s.connect((host,port))
    while True:
        if count < 5:
            s.sendall(payload1)
            print("Packet " + str(count))
        elif count == 10:
            s.sendall(payload1)
            print("Packet " + str(count))
            count = 0
        elif count >= 5:
            s.sendall(payload2)
            print("Packet " + str(count))
        reply = s.recv(2048)
        if b"""HACKED!""" in reply:
            print("HACKED!")
            break
        sleep(random.uniform(0.0,5.0))
        count += 1
