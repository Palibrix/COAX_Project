import socket

from conndata import Connection


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Connection.HOST, Connection.PORT))

    # s.sendall(b'Hi, input, I`m output')

    s.sendall(b'Receive')
    data = s.recv(1024); print(f"Received {data!r} ")
