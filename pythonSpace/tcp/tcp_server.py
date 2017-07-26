import socket
import threading

import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        stopword = ''
        serverData = ''
        for line in iter(input, stopword):
            serverData += line + '\n'
        # serverData = input('server: ')
        print('server: ', serverData)
        sock.send(serverData.encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

def receiver(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('client: ', data.decode('utf-8'))
    sock.close()
    # print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.90.24.64', 9999))
s.listen(5)
print('Waiting for connection...')

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    receiver = threading.Thread(target=receiver, args=(sock, addr))
    t.start()
    receiver.start()


