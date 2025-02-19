#!/usr/bin/python
# Filename : tuple_demo.py

## 演示tuple 元组的基本操作
### 元组（Tuple）用于将多个对象保存到一起。你可以将它们近似地看作列表，但是元组不能提供列表类能够提供给你的广泛的功能。
### 元组的一大特征类似于字符串，它们是不可变的，也就是说，你不能编辑或更改元组

### 元组是通过特别指定项目来定义的，在指定项目时，你可以给它们加上括号，并在括号内部用逗号进行分隔。
#### 元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，意即元组内的数值不会改变。

zoo =("python","penguin","elephant")
## 如果是空元组则，zoo=() 
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

## 如果是1个项目的元组，则zoo=("penguin",) 
onezoo=("penguin",) 
print('All animals in onezoo are', onezoo)
print('Number of cages in the neonezoo is', len(onezoo))
