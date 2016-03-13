import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = 'localhost', 10000
sock.bind(addr)
sock.listen(3)
while True:
    connection, client_address = sock.accept()
    data = connection.recv(100000)
    print(data)
    f = open("website.html","w")
    f.write(data.decode('utf-8'))
