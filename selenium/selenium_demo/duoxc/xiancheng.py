
import threading

class Xianchen():
    """python 多线程操作"""
    

    def command_run(self,i):
        """定义多线程执行的函数"""

        print("程序"+str(i)+"进行执行")


    def start(self):
        """开始执行"""
        nthreds = []
        for i in range(10):
            print("生成线程")
            t = threading.Thread(target=self.command_run,args=(i,))

            nthreds.append(t)


        return nthreds

if __name__ =="__main__":
    print("开启多线程")
    xc = Xianchen()
    nthreads = xc.start()
    for t in nthreads:
        t.start()


