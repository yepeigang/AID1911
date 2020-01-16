from socket import *
from baidu import *

def handle(c):
    image_type = c.recv(1024).decode()
    f = open("img.jpg",'wb')
    while True:
        data = c.recv(1024)
        if data == b'##':
            break
        f.write(data)
    f.close()
    msg = baidu(image_type,'./img.jpg')
    if image_type == '其他':
        c.send(msg[0].get('Keyword','Sorry').encode())
    else:
        c.send(msg[0].get('name','Sorry').encode())

s = socket()
s.bind(('127.0.0.1',8887))
s.listen(3)

while True:
    c,addr = s.accept()
    print("Connect from",addr)
    handle(c)
    c.close()

