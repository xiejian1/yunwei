


class logging(object):

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(func=self.func.__name__))
        print(args[0])
        return self.func(*args,**kwargs)

@logging
def say(something):
    print("打印信息")


if __name__ =="__main__":
    say("西昌 一座春天栖息的城市!")
