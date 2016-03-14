import socket
import re
addr = ('localhost',10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect(addr)
        alldata = []
        lines = 0
        f = open("main.html","r")
        for line in f:
            alldata.append(line)
            lines+=1
        msg = "".join(alldata)
        msg = re.sub('\n', '', msg)
        sock.sendall(msg.encode('utf-8'))
    except:
        pass
