

from queue import Queue

class Duilie():
    """队列的使用"""



    def q_duilie(self):
        """队列的基本操作"""
        q = Queue()
        for i in range(10):
            print("队列存入10个数")
            q.put(i)

        print("打印队列里面的消息")
        while not q.empty():
            print(q.get())


if __name__ == "__main__":
    duilie = Duilie()
    duilie.q_duilie()