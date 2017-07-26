import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('10.90.24.64', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while(True):
    # 发送数据:
    data = input('client: ')
    s.send(data.encode('utf-8'))
    # print('client: ', data)
    if not data or data == 'exit':
        break
    print('server: ', s.recv(1024).decode('utf-8'))
# s.send(b'exit')
s.close()