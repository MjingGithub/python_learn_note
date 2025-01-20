#!/usr/bin/python
# Filename : dict_demo.py

## 演示字典的基本操作
### 字典的keys必须是唯一的，且不可变的，比如字符串，但是你可以使用可变或不可变的对象作为字典中的值
### 形式为：d = {key : value1 , key2 : value2} 

# “ab”是地址（Address）簿（Book）的缩写
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])
# 删除一对键值—值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
