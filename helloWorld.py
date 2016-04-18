#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# basic data tye: string, byte, floating, integer, boolean(True/False), None
print("hello, world")
print(123e15)
print('I\'m "ok"')
print('\\\\ok')
print(r'\\\\ok')
print('''different
lines
ok?''')
print(r'''different
lines
ok?''')
print(3 > 2)
print(3 > 2 or 2 > 3 and 5 > 4)
print(not 3 > 2)
print(None)

# practice
n = 123
f = 456.789
s1 = 'hello,world'
s2 = 'hello,\'adam\''
# here 'r' is used to stop ESC(escape character) take into effect
s3 = r'hello,\'bart\''
# it should be same no matter with 'r' or without 'r'
s4 = r'''hello,
lisa!'''
print("practice")
# string '+' number doesn't work
print("n:", n)
print("f:", f)
# string '+' string still work with concat effect
print("s1:" + s1)
print("s2:" + s2)
print("s3:" + s3)
print("s4:" + s4)

# string coding translation
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

# string encode
# [string -> byte] (ascii - 1 byte, unicode - 2 bytes, utf-8 - 1-6 bytes(english -  1 byte, chinese - 3 bytes))
print('ABC')  # ABC
print(b'ABC')  # b'ABC', use one byte to store one character
# print('中文'.encode('ascii')) this will not work since ascii has not encoded chinese
print('ABC'.encode('ascii'))  # b'ABC', 使用ascii把ABC编码成bytes
print('ABC'.encode('utf-8'))  # b'ABC', 使用utf-8把ABC编码成bytes, 由于是纯英文字符，所以utf-8与ascii一样每个字符都只占用一个byte
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87', 非英文字符会转变成16进制编码，每个中文字符占用三个bytes
print('中ABC文'.encode('utf-8'))  # b'\xe4\xb8\xadABC\xe6\x96\x87'
# print('中文'.encode('unicode')) this will not work since python has already encoded string with unicode in default

# String decode
# [byte -> string]
print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('ascii')) these bytes can't be decoded as ascii
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# string/bytes length
print("'ABC''s length is", len('ABC'))
print("'中文''s length is", len('中文'))
print("b'ABC' are bytes, its length is", len(b'ABC'))
print(r"b'\xe4\xb8\xadABC\xe6\x96\x87' are bytes, its length is", len(b'\xe4\xb8\xadABC\xe6\x96\x87'))

# usage of %
print('%%s')  # there is no problem to use % in string without any format attached
print('%s' % 'format string')  # when there is mapping value outside, then % take into effect
print('%s %%' % 'format string')  # %% will escape %
print('%s' % 15)  # string
print('%d' % 15)  # integer
print('%x' % 15)  # hexadecimal
print('%f' % 15)  # floating
print('%s %d %x %f' % (15, 15, 15, 15))  # combined
print('%s %s %s %s %s' % (True, b"i'm byte", 15, 15.2, None))  # all other basic type can be translated to string

# list (索引从0开始对应第一个元素，然后递增，或者从-1开始对应最后一个元素，然后递减)
classmates = ['maple', 'wang', 'feng']
print(classmates)
print("length:", len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
classmates.append(15)  # list是一个可变的有序表，所以，可以往list中追加元素到末尾,注意返回值为None
print(classmates)
classmates.insert(1, 16)  # 可以把元素插入到指定的位置，比如索引号为1的位置，注意返回值为None
print(classmates)
print(classmates.pop())  # 删除list末尾的元素,返回值为最后一个元素
print(classmates.pop(1))  # 返回值为指定的删除的元素
print(classmates)
classmates2 = [1, 2, 3]
print(classmates + classmates2)  # 两个list可以相加，注意python中+两边的数据类型必须一致才能生效
classmates.append(classmates2)  # list的元素可以是不同的数据类型，当然也包括list
print(classmates)
print(classmates[0][0], classmates[1][2], classmates[2][3], classmates[3][2])  # 字符串也相当于是一个list

# tuple （元组：另一种有序列表，tuple和list非常类似，tuple一旦初始化就不能修改）
classmates = ('maple', 'wang', 'feng')
print(classmates)
emptyTuple = ()  # empty tuple
print(emptyTuple)
# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
oneElementTuple = ('maple',)
print(oneElementTuple)
print(oneElementTuple[0])  # tuple是一种有序列表
tupleInList = [oneElementTuple, classmates]
print(tupleInList)
print(tupleInList[0][0][0])
classmates2 = ('x', 'y')
print(classmates + classmates2)  # tuple可以直接相加

# practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# print Apple
print(L[0][0])
# print Python
print(L[1][1])
# print Lisa
print(L[2][2])

# 条件判断 conditional judgement
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
age = 6
print("your age is", age)
if age >= 18:
    print('adult')
elif age >= 10:
    print("juvenile")
else:
    print("teenager")

# birth = input('birth: ') is string, can be used to compare with int
# birth = int(input('birth: '))
birth = 1985
if birth < 2000:
    print('00前')
else:
    print('00后')

# practice
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 28:
    print("overweight")
elif bmi < 32:
    print("obesity")
else:
    print("severe obesity")

# 循环 cycle
for x in [19, 'maple', True]:
    print(x)
sum = 0
for x in range(101):  # 0~100, 也可以list(range(101))
    sum += x
print(sum)
sum = 0
x = 100
while x > 0:
    sum += x
    x -= 1  # 不能用--x或者x--吗？
print(sum)

# practice
for x in ['Bart', 'Lisa', 'Adam']:
    print("Hello,", x)

# dict: python中的map，key-value，key的集合是一个set，一个key只对应一个value
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Bob'])  # 通过key来找value，方法1
print(d.get('Bob'))  # 通过key来找value，方法2
d['Bob'] = 14  # set value
print(d['Bob'])
if 'Maple' in d:  # 判断key是否存在的方法1
    print("Maple is in", d)
else:
    print("maple is not in", d)
if d.get('maple'):  # 判断key是否存在的方法2, 没有会返回None
    print("Maple is in", d)
else:
    print("maple is not in", d)
d.pop('Bob')  # 删除一个key-value pair
print(d)
d2 = {'maple': 10, 'wang': 20}
print(d2)
# print(d+d2) 不支持两个dict之间相加
# print(d&d2) 不支持两个dict之间与
# print(d|d2) 不支持两个dict之间或
'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
'''

# set : set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = {1, 1, 2, 2, 3, 3}  # 创建set方法1，没有value的dict，重复的元素会被自动过滤
# s = {[1,1,2,2,3,3]} # list是可变数据类型，不能作为set的元素
s = set([1, 1, 2, 2, 3, 3])  # 创建set方法2，输入一个list
print(s)
s.add('maple')  # 为set add一个元素，如重复会自动过滤，注意返回为None
print(s)
s.remove('maple')  # 删除一个元素,返回为None
print(s)
s2 = {'maple', 'wang'}
print(s2)
# print(s+s2) 两个set不能直接相加
print(s & s2)  # 两个set可以与
print(s | s2)  # 两个set可以或

# practice
d = {(1, 2, 3): 20}
a = (1, 2, 3)
print(d[a])
a = ('maple', 'wang')
s = {a}
print(s)
print({(1, 2), (1, 2, 3)})
# tuple可以为set的元素，也可以为dict的key
# print({(1,2),(1,[2,3])}) 即使(1,[2,3])为tuple，但是它里面含有list，为可变对象，就不能使用
'''
不可变对象： 所有的基本数据类型（string, None, boolean, integer, floating, byte）, tuple(元素可以为任意的)
可变对象： list(元素可以为任意的)， set（元素必须是完全不可变对象，比如tuple中元素也要为不可变对象），
dict（key必须要是不可变对象，value可以为任意的）
'''


# built-in functions https://docs.python.org/3/library/functions.html
# built-in constants https://docs.python.org/3/library/constants.html
# built-in type https://docs.python.org/3/library/stdtypes.html

# define function
def test(x):
    print(x)
    return


test("just test function")
'''
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

return None可以简写为return
'''


def nop():
    pass  # 占位符，如果缺少return，必须要有pass才行
    return


nop()


def returnMultipleValues():
    return 1, 2, 3


print(returnMultipleValues())  # 实际返回的是一个tuple


# parameter type for function

# 位置参数：指的是必选参数，调用的顺序必须要和定义的顺序相同
def power(x):
    return x * x


print(power(x=10))  # 位置参数可以带参数名称，但是带不带参数名称是可选的
print(power(10))


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(10, 4))


# 默认参数：定义的参数可以有默认值，所以是可选参数，必须定义在所有必选参数之后
def power2(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power2(10))
print(power2(10, 3))
'''
从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
'''


def enroll(name, gender, age=6, city='Shanghai'):
    print(name)
    print(gender)
    print(age)
    print(city)


enroll('maple', 'male')  # 不带参数名，参数的位置必须与定义的一致
enroll(gender='male', name='maple', age=30)  # 如果带上参数名，那么参数的位置不必为定义的顺序
enroll('maple', 'male', city='Hangzhou')  # 如果默认参数有多个，而调用的时候又不全部调用，那么最好把调用参数的名称写上


def addEnd(L=[]):
    L.append('end')
    return L


print(addEnd())
print(addEnd())
print(addEnd())
'''
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def addEnd(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(addEnd())
print(addEnd())
print(addEnd())


# 可变参数：传入的参数的个数是可变的，所有的传入的参数被组合成一个tuple
def calc(*num):
    s = 0
    for x in num:
        s += pow(x, 2)
    return s


print(calc(1, 2, 3, 4))
'''
在函数内部，参数num接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
'''


def printNum(*num):
    print(num)  # num会是一个tuple
    for x in num:
        print(x)  # num的元素可以是任意的类型


printNum(1, 3, True, [1, 2], {"maple": 10, "wang": 20}, {10, 20})
num = (1, 3, True, [1, 2], {"maple": 10, "wang": 20}, {10, 20})
# 如果已经得到了一个tuple，而要用一个可变参数的函数
printNum(num)  # 只被认为是一个tuple元素
printNum(*num)  # *num会被解析一个列表
print(*num)  # *num会是一个参数列表
printNum()  # 0个参数即为()


# 关键字参数：传入的参数的个数是可变的，并且允许带参数名称，在函数内部，会被组装成dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("maple", 24)
person("maple", 24, height=172, weight=65)
person(height=172, name="maple", weight=65, age=24)  # 使用了参数名，顺序不用和定义的一样
# 如果dict已经组装好，则使用**来作为参数输入
others = {'height': 172, 'weight': 65}
person("feng", 30, **others)


# 命名关键字参数：和关键字参数**kw不同，定义的时候，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)


person2("maple", 15, city='shanghai', job='free')  # 都是必选的参数，与位置参数不同的是命名关键字参数在调用的时候必须带有参数名


def person3(name, age, *, city='hangzhou', job='engineer'):  # 命名关键字参数可以是默认参数
    print(name, age, city, job)


person3('maple', 16)

'''
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
'''

# this is just change for test
