#!/usr/bin/python
# Filename : sequence_operate.py

## 序列的主要功能是资格测试（Membership Test）（也就是 in 与 not in 表达式）和索引操作（Indexing Operations），
## 它们能够允许我们直接获取序列中的特定项目

### 上面所提到的序列的三种形态——列表、元组与字符串，同样拥有一种切片（Slicing）运算符，它能够允许我们序列中的某段切片——也就是序列之中的一部分。

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

### 你同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）：
### 当步长为 2 时，我们得到的是第 0、2、4…… 位项目

print('Item 1 to end with step 2 is', shoplist[1::2])
print('Item 1 to end with step 2 is', shoplist[1:3:2])