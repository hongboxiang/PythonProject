import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.90.24.64', 9999))
print('Bind UDP on 9999...')
data = 'data'
while(data and data != 'exit'):
    ser_data = input('server: ')
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    print('Received from %s:%s.' % addr)
    s.sendto(ser_data.encode('utf-8'), addr)