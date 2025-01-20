#在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。因此，还有一个
## with 语句使得这一过程可以以一种干净的姿态得以完成。

## 我们将关闭文件的操作交由 with open 来自动完成。
### 它总会在代码块开始之前调用 thefile.__enter__ 函数，并且总会在代码块执行完毕之后调用 thefile.__exit__ 。
with open("poem.txt") as f:
    for line in f:
        print(line, end='')