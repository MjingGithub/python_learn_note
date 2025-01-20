#!/usr/bin/python
# Filename : modules.py

## 如果你想在你所编写的别的程序中重用一些函数的话，应该怎么办？答案是模块（Modules）
# 如何使用标准库模块
### sys 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的系统功能（system）
import sys
import os

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
# 查看你的程序目前所处在的目录
print(os.getcwd())

# from .. import 语句
## 如果你希望直接将 argv 变量导入你的程序（为了避免每次都要输入 sys. ），那么你可以通过使用 from sys import argv 语句来实现这一点。
### 但是最好不这样使用，避免名称冲突
from math import sqrt
print("Square root of 16 is ",sqrt(16))

## 每个模块都有__name__，这对于确定模块是独立运行的还是被导入进来运行的这一特定目的来说大为有用
print(sys.__name__)
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

# dir()函数，能够返回由对象所定义的名称列表，如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量
# # 该函数接受参数。 如果参数是模块名称，函数将返回这一指定模块的名称列表。 如果没有提供参数，函数将返回当前模块的名称列表。
print(dir(sys))
print(dir())
