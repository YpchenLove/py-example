import sys

str = 'Ypchen'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])

print(str * 2)
print(str + '很帅')

print('hello\nstr')
print(r'hello\nstr')

sys.stdout.write(str + '\n')

print('str', end=" ")
print('str', end=" ")

# input("\n\n按下 enter 键后退出。")

# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。

print("我叫%s 你是%s" % ('小明', '沙雕'))

print(str.center(20, '❤'))
