from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',8887))

while True:
    image_type = input("图片类型:")
    if image_type in ['动物','植物','其他']:
        break
file = input("图片:")
f = open(file,'rb')
s.send(image_type.encode())
sleep(0.1)
while True:
    data = f.read(1024)
    if not data:
        sleep(0.1)
        s.send(b'##')
        break
    s.send(data)
r = s.recv(1024).decode()
print("这是:",r)
