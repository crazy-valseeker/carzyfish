
#装饰器的用法  可以用来做AOP

def funaop(callback):
    count=1
    def test(*argv):
        print("function aop test")
        nonlocal callback
        callback(*argv)
        pass
    return test

@funaop
def func(str):
    print(str)
    pass

func("test str")


#类的aop

class A:
    def __init__(self):
        self.cStr="class A before modify"
        pass

    def atest(self,nStr):
        print(self.cStr)
        print(nStr)
        pass

    @funaop
    def changeStr(self):
        self.cStr="class A after modify"
        pass

a=A()
a.atest("cStr")
a.changeStr()
a.atest("cStr")