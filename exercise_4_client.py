from socket import *
import time

ADDR = ('127.0.0.1',8888)

filename = input(">>")

f = open(filename,'rb')

s = socket()
s.connect(ADDR)

while True:
    data = f.read(1024)
    if not data:
        time.sleep(0.5)
        s.send(b'##')
        break
    s.send(data)

f.close()

msg = s.recv(1024) #　等结果
print("检测结果：",msg.decode())

s.close()