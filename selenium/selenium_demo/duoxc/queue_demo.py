import queue
import threading
import time
exitFlag = 0
workQueue = queue.Queue(10)
queueLock = threading.Lock()
class Mythread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q


    def run(self):
        print("开启线程："+self.name)
        process_data(self.name,self.q)
        print("退出线程:"+self.name)

def process_data(threadName,q):

    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s"%(threadName,data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ['Thread-1','Thread-2','Thread-3']
nameList = ['One','Two','Three','Four','Five']
threads = []
threadID = 1

#创建线程
for tName in threadList:
    thread = Mythread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1

#填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass

#通知线程退出
exitFlag = 1

#等待所有线程完成
for t in threads:
    t.join()
print("退出线程")