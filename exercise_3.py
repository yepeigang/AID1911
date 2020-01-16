import os

DIR = "/home/tarena/备份/"
dir = input(">>") # 要备份的目录
if dir[-1] != '/':
    dir += '/'

#　复制文件
def copy(file):
    fr = open(dir+file,'rb')
    fw = open(DIR+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

def main():
    file_list = os.listdir(dir) # 得到文件列表
    for file in  file_list:
        #判断一个文件是否为普通文件
        if os.path.isfile(dir+file):
            copy(file) #　复制文件


if __name__ == '__main__':
    main()
