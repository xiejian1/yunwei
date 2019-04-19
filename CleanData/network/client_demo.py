import socket


class Connect():
    """连接服务器"""
    def __init__(self,ip='localhost',port=8000):

        self.ip = ip
        self.port = port

    def conn(self):
        print("创建套接字对象")
        s = socket.socket()
        s.connect((self.ip,self.port))
        return s

    def receiveMsg(self):
        """接收消息"""
        flag = True
        s = self.conn()
        print("开始接收消息")
        print("获取本地地址",s.getsockname()[0])
        while flag:
            data = self.sendMsg()
            if data == 'q':
                flag = False
                s.close()
            else:
                s.send(data.encode("utf-8"))
                print("等待接收数据....: ")
                msg = s.recv(1024)
                print("返回数据: ",msg.decode("utf-8"))

    def sendMsg(self):
        """发送消息"""
        data = input("请输入数据: ")
        return data
if __name__ =="__main__":
    connect = Connect(ip='192.168.173.177',port=8000)
    connect.receiveMsg()