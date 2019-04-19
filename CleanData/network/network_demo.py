import socket

class ServerDemo():

    """套接字demo"""
    def __init__(self,ip='localhost',port=8000):
        """添加ip地址"""
        self.ip = ip
        self.port = port
    def startup(self):
        print("创建套接字对象")
        s = socket.socket(family=socket.AF_INET)
        s.bind((self.ip,self.port))
        s.listen(5)

        return s
    def receive(self):
        """接收数据"""
        print("服务器开始启动")
        print(".......")
        s = self.startup()
        print("获取本地地址",s.getsockname()[0])
        print("服务器启动完成，等待连接")
        while True:
            """等待客户端来进行链接,并且创建socket对象"""
            print("等待接收数据")
            c,addr = s.accept()
            print("是由远程地址："+addr[0]+" 进行链接")
            data = c.recv(1024)
            print("%s:%s"%(addr[0],data.decode("utf-8")))
            msg = "您好，"+addr[0]+" 欢迎连接到服务器"
            c.send(msg.encode("utf-8"))
            c.close()



if __name__ =="__main__":
    server = ServerDemo(ip='192.168.173.177',port=8000)
    server.receive()