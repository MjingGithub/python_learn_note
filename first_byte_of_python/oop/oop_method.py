# 类方法第一个参数，一定是self,代表对象自身
class Person:
    def say_hi(self):
        print('Hello ,how are you ?')

p=Person()
p.say_hi()