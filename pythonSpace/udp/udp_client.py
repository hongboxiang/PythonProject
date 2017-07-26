import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'data'
while(data and data != 'exit'):
    data = input('client: ')
    # 发送数据:
    s.sendto(data.encode('utf-8'), ('10.90.24.64', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
