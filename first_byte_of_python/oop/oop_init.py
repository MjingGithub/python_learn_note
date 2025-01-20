# __init__ 方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想
#进行操作的目标对象进行初始化（Initialization）操作。这里你要注意在 init 前后加上的双下划线。

class Person:
    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print('Hello,my name is',self.name)

p=Person("Alice")
p.say_hi()