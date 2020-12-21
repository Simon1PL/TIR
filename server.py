import socket
host = '127.0.0.1'
port = 1883
s = socket.socket()
s.bind((host, port))
s.listen(60)
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    print("received data:", data)
    conn.send(data)
    conn.close()
