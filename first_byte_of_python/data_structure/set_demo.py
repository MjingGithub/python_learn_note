#!/usr/bin/python
# Filename : set_demo.py

## 集合（Set）是简单对象的无序集合（Collection）。当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就会使用集合。
## 通过使用集合，你可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到两个集合的交集，等等。

bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

bric = bri.copy()
bric.add('china')
# 是否是子集 bri 是 bric的子集
print(bric.issuperset(bri))

bri.remove('russia')
 # 交集
print(bri & bric) # or bri.intersection(bric)