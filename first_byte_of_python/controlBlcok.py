#!/usr/bin/python
# Filename : controlBlock.py

# if,while,for 控制流语句使用

# if语句
number = 23

choose = input('Choose a block,if,while or for: ')
if(choose=='if'):
    guess = int(input('Enter an integer : '))

    if(guess==number):
        #新块从这里开始
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
    elif guess<number:
        #另一代码块
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')

    print("Done")

#  while 语句:while 语句同样可以拥有 else 子句作为可选选项
elif(choose=='while'):
    runnning = True
    while runnning:
        guess = int(input('Enter an integer : '))
        if guess == number:
            print('Congratulations, you guessed it.')
            # 这将导致 while 循环中止
            runnning = False
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    else:
        print('The while loop is over.')
    print("Done")

elif(choose=='for'):
    for i in range(1,5):
        print(i)
    else:
        print('The for loop is over')