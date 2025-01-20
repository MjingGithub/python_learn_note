def getErr():
    return (2,"errors")

errorNum,errstr = getErr()
# 要注意到 a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的一个元组。
print("errorNum:{},errstr:{}".format(errorNum,errstr))

#这也意味着在 Python 中交换两个变量的最快方法是：

a=5
b=8
print("a:{},b:{}".format(a,b))
(a,b) = (b,a)
print("a:{},b:{}".format(a,b))
