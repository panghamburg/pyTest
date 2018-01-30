import sys
import socket

servicesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

servicesocket.bind((host, port))

servicesocket.listen(3)

while True:
    clientsocket, addr = servicesocket.accept()
    print('连接地址：%s' % str(addr))
    msg = 'Hello' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
