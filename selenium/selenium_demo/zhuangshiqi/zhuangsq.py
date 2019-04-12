

class Zhuangsq():
    """装饰器的设计"""

    def debug(self):
        import inspect
        caller_name = inspect.stack()[1][3]
        print("[DEBUG]: enter {}()".format(caller_name))

    def say_hello(self):
        self.debug()
        print("hello!")
    def say_goodbye(self):
        self.debug()
        print("goodbye!")


def dec(func):
    def wrapper(something):
        print("[DEBUG]:enter {}()".format(func.__name__))
        print("hello the world",something)
        return func(something)
    return wrapper
@dec
def decorate_demo(something):
    print("hello world!")

def decor_demo(func):

    def wrapper(*args,**kwargs):
        print("装饰器设计")
        print('Prepare and say....')
        print(kwargs['hello'])

        return func(*args,**kwargs)
    return wrapper

@decor_demo
def decor_test(hello=''):
    print("打印消息",hello)






if __name__ == "__main__":
    # zhuangsq = Zhuangsq()
    # zhuangsq.say_hello()
    # zhuangsq.say_goodbye()
    decor_test(hello="xi chang is a city where Spring stays!")