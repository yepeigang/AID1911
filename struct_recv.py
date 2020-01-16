"""
 使用udp 和 struct模块
      1. 从客户端循环录入学生信息，包含

         id   姓名  年龄   分数

      2. 将信息打包发送给服务端

      3. 在服务端判断如果学生的分数大于90分则将该学生
      信息写入到 student.txt文件中
      每位学生信息占一行
"""
from socket import *
import struct

# 与客户端协商后的格式  id name  age  score
st = struct.Struct("i32sif")

# udp 套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

# 打开文件
f = open("student.txt",'a')

while True:
    data,addr = s.recvfrom(1024)
    # data-->bytes (1,b'lily',18,92.5)
    data = st.unpack(data)
    if data[3] >= 90:
        name = data[1].decode().strip('\x00')
        info = "%d   %s    %d   %.1f\n"%(data[0],name,data[2],data[3])
        f.write(info)
        f.flush()

f.close()
s.close()







