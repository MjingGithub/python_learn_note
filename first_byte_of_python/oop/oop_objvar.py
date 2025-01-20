#类变量（Class Variable）是共享的（Shared）——它们可以被属于该类的所有实例访问。
## 该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现。
### self.__class__.population.
#对象变量（Object variable）由类的每一个独立的对象或实例所拥有。在这种情况下，每个
## 对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，也不会以任何方式与其它不同实例中的相同名称的字段产生关联。
class Robot:
    """ 表示一个带有名字的机器人 """

    # 一个类变量，用来计数机器人的数量
    population=0

    def __init__(self,name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人将会增加人口数量
        Robot.population+=1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name)) 

        Robot.population-=1

        if Robot.population==0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(self.__class__.population))

    def say_hi(self):
       """来自机器人的诚挚问候
        没问题，你做得到。"""
       print("Greetings, my masters call me {}.".format(self.name))

# how_many 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个classmethod（类方法） 或是一个 staticmethod（静态方法） ，
## 既不需要访问类属性，也不需要调用实例属性，则可以声明静态方法：
### 静态方法既不需要传递类对象也不需要传递实例对账（self/cls）
    @staticmethod
    def how_many(population):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(population))

    @classmethod
    def how_many1(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
droid1.how_many(droid1.population)

droid2 = Robot("C-3PO")
droid2.say_hi()
droid2.how_many(droid2.population)

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many1()

