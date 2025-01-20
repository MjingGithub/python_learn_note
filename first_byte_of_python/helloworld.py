#!/usr/bin/python
# Filename : helloworld.py

print ('Hello World')

# var 变量使用
i = 5
print(i)
i = i + 1
print (i)

# 利用三引号，你可以指示一个多行的字符串。你可以在三引号中自由的使用单引号和双引号
s = '''This is a multi-line string.
This is the second line.'''
print (s)
s='''This is a multi-line string. This is the first line. This is the second line. "What's your name?," I asked.'''
print (s)

# 默认一个物理行只写一句逻辑行，比如：
i = 5
print(i)

# 如果你想要在一个物理行中使用多于一个逻辑行，那么你需要使用分号（;）来特别地标明这种用法。分号表示一个逻辑行/语句的结束。例如：
i = 5; print(i)

# 下面是一个在多个物理行中写一个逻辑行的例子。它被称为明确的行连接。
s = 'This is a string. \
This continues the string.'
print(s)

# 缩进，空白在Python中是重要的。事实上行首的空白是重要的。它称为缩进。在逻辑行首的空白（空格和制表符）用来决定逻辑行的缩进层次，从而用来决定语句的分组。
##  这意味着同一层次的语句必须有相同的缩进。每一组这样的语句称为一个块。我们将在后面的章节中看到有关块的用处的例子


