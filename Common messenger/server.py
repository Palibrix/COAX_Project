import socket;

from conndata import Connection

prevData = b''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Connection.HOST, Connection.PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(f"data:{data}")
            print(f"prevData: {prevData}")
            if data == b'Receive':
                conn.sendall(prevData)
            if not data:
                conn, addr = s.accept()
            if data != b'':
                if data != b'Receive':
                    prevData = data
            print(f"prevData: {prevData} at the and")