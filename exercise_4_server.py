from socket import *

#　我的容器
class Mylist:
    def __init__(self):
        self.__elem = []

    def push(self,val):
        self.__elem.append(val)

    def pop(self):
        return self.__elem.pop()

    def empty(self):
        return self.__elem == []


# 判断结果
class Ver:
    def __init__(self):
        self.parens = "{}[]()"
        self.left_parens = "{[("
        #　关系匹配字典
        self.opposite = {'}':'{',']':'[',')':'('}
        self.vessel = Mylist()

    #　遍历文本 (生成器函数)
    def parent(self,text):
        # i 记录遍历的位置
        i,text_len = 0,len(text)
        while True:
            #　循环的遍历文本
            while i < text_len and text[i] not in self.parens:
                i += 1

            if i >= text_len:
                return
            else:
                yield text[i],i
                i += 1

    #　验证括号
    def ver(self,text):
        for pr,i in self.parent(text):
            if pr in self.left_parens:
                self.vessel.push((pr,i)) #　左括号
            elif self.vessel.empty() or self.vessel.pop()[0] != self.opposite[pr]:
                return "在%d位置括号%s错误"%(i,pr)

        if self.vessel.empty():
            return "完全正确"
        else:
            p = self.vessel.pop()
            return "在%d位置括号%s错误" %(p[1],p[0])




# 创建套接字，收文件，发结果
def main():
    s = socket()
    s.bind(('0.0.0.0',8888))
    s.listen(3)
    while True:
        text = ""
        c,addr = s.accept()
        while True:
            data = c.recv(1024).decode()
            if data == '##':
                break
            text += data
        v = Ver() #　判断括号正确性
        result = v.ver(text)
        c.send(result.encode())


if __name__ == '__main__':
    main()