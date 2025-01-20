#!/usr/bin/python
# Filename : reference_demo.py

## 当你创建了一个对象并将其分配给某个变量时，变量只会查阅（Refer）某个对象，并且它也不会代表对象本身。
## 也就是说，变量名只是指向你计算机内存中存储了相应对象的那一部分。这叫作将名称绑定（Binding）给那一个对象。
### 一般来说，你不需要去关心这个，不过由于这一引用操作困难会产生某些微妙的效果，这是需要你注意的：
### 要记住列表的赋值语句不会创建一份副本。你必须使用切片操作来生成一份序列的副本
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 二者都删除了第一个项目

print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同