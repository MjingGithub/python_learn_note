#!/usr/bin/python
# Filename : functions.py

# def定义函数

def print_max(a,b):
    if a>b:
        print(a,"is maximum")
    elif a==b:
        print(a,'is equal to',b)
    else:
        print(b,'is maximum')

print_max(5,7)

x=4
y=7
print_max(x,y)
    
# 局部变量
# 这些变量名只存在于函数这一局部（Local）。这被称为变量的
# 作用域（Scope）。所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。

x=50

def func(x):
    ## x is  50
    print('x is ',x)
    x=2
    ## changed local x to 2
    print('changed local x to',x)
func(x)
##  x is still  50
print('x is still ',x)

# global 变量：如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的

x=50

def func_global():
    global x
    ## x is  50
    print('x is ',x)
    x=2
    ## changed local x to 2
    print('changed global x to',x)
func_global()
##  x is still  50
print('x is now changed to ',x)

# 默认参数值：你可以通过在函数定义时附加一个赋值运算符（ = ）来为参数指定默认参数值。默认参数值应该是不可变的
### 注意:只有那些位于参数列表末尾的参数才能被赋予默认参数值，这是因为值是按参数所处的位置依次分配的。举例来说， def func(a, b=5) 是有效的，但 def func(a=5, b) 是无效的。
def func_default(message,times=1):
    print(message * times)
func_default("hello")
func_default("hello",5)

# 关键字参数：如果你有一些具有许多参数的函数，而你又希望只对其中的一些进行指定，我们使用命名（关键字）而非位置（一直以来我们所使用的方式）来指定函数中的参数

def func_keywords(a,b=5,c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func_keywords(3, 7)
func_keywords(25, c=24)
func_keywords(c=50, a=100)

# 可变参数：可以通过使用星号来实现
## 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
### 类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary
def total(a=5,*numbers,**phonebook):
    print("a=",a)
    # 遍历numbrs元组中的所有数据
    for single_item in numbers:
        print("single_item:",single_item)
    # 遍历phonebook字典中的所有数据
    for first_part,second_part in phonebook.items():
        print("first_part:",first_part,",second_part:",second_part)

total(10,1,2,3,Jack=111,John=555,Alice=999)


# DocStrings:文档字符串,DocStrings 是一款你应当使用的重要工具，它能够帮助你更好地记录程序并让其更加易于理解。
# ## 令人惊叹的是，当程序实际运行时，我们甚至可以通过一个函数来获取文档！
def func_docstring(x,y):
    ### 文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明。
    #### 在此强烈建议你在你所有重要功能的所有文档字符串中都遵循这一约定。
    ##### 我们可以通过使用函数的__doc__
    '''打印2个值中的最大数。

    这2个数都应该是整数。'''
    # 如果可能将其转换成整数类型
    x=int(x)
    y=int(y)
    if x>y:
        return x
    else:
        return y
    
maximum = func_docstring(3,5)
print(maximum,"is maximum")
print(func_docstring.__doc__)
### help帮助文档就是利用了DocStrings去展示，比如：
help(func_docstring)


