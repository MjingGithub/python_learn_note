#!/usr/bin/python
# Filename : list_demo.py

## 演示list 列表的基本操作

myShippingCart = ["apple","pants","shoes"]

## 在这里要注意在调用 print 函数时我们使用 end 参数，这样就能通过一个空格来结束输出工作，而不是通常的换行。
print('These items are:', end=' ')

for item in myShippingCart:
    print(item, end=' ')

print('\nI also have to buy rice.')
myShippingCart.append('rice')
print('My shopping list is now', myShippingCart)

print('I will sort my list now')
myShippingCart.sort()
print('Sorted shopping list is', myShippingCart)

print('The first item I will buy is', myShippingCart[0])
olditem = myShippingCart[0]
del myShippingCart[0]
print('I bought the', olditem)
print('My shopping list is now', myShippingCart)