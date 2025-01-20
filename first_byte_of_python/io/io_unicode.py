# encoding=utf-8
## 当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们
### 的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"中国深圳，财富港")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)