import socket
from time import sleep

host = "192.168.10.233"
port = 1433

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    print("Bound to " + host + ":" + str(port))
    s.listen()
    conn,addr = s.accept()
    with conn:
        count = 1
        pwned = b"""commence hacking"""
        expected1 = b"""\x00\x00\x00Innocent Packet\x00\x00\x00"""
        expected2 = b"""\x00\x00\x00Vulnerable Packet\x00\x00\x00"""
        while count <= 10:
            data = bytes(conn.recv(2048))
            if pwned in data:
                conn.sendall(bytes("\x00\x00\x00HACKED!\x00\x00\x00",encoding='utf-8'))
                print("HACKED!")
                break
            elif expected1 in data:
                conn.sendall(bytes("\x00\x00\x00Packet Response " + str(count) + "\x00\x00\x00",encoding='utf-8'))
                print("Packet " + str(count))
            elif expected2 in data:
                conn.sendall(bytes("\x00\x00\x00Hacking Failed\x00\x00\x00",encoding='utf-8'))
                print("Hacking failed")
            else:
                print("Unexpected client packet!")
                break
            count += 1
            if count == 10:
                count = 1