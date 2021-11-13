# 变量定义不需要声明类型
a='hello world'
print(a)
a=123
print(a)

# 给多个变量赋值
a=b=c=1
print(a)
print(b)
print(c)
a,b,c=1,2,"31"
print(a)
print(b)
print(c)

# list有序数组类型, 元素类型可以不同，可以是数组
names=["测试","你好", "lxc", 214, 99]
print(names)
print(len(names))
print(names[1:2]) # 截取从1开始，到2结束，不包括下标2
print(names[:])
names[1]="你好11" # 修改元素
names.append('哈哈') #添加元素
del names[5-1] # 通过下标删除元素
#列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表,复制最低是2,
# names=names + [1,2]
# print(names*2)
names.insert(0, "66")

# 元组 包在校括号里面，一个元素时后面要加上逗号；里面的元素不可修改，tuple 所谓的“不变”是说，tuple 的每个元素指向不变
# 通过下标访问数据，可间接修改元素
# 与列表一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
tuple=(1, 2, "lihao", names)
print(tuple)
names[0]="666"
del tuple #删除整个元组
print(tuple)
# 和列表异同: 运算符和内置函数相似，区别是不能添加、修改、删除元素

# dict
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
# dict = {key1 : value1, key2 : value2 }
# 注意：键必须是唯一的，键可以是字符串、数字、元组类型，不能是列表，但值则不必。值可以取任何数据类型，但键必须是不可变的。
# 键不能重复，若重复了，以最后一个为准
# 类似于java中的map

nameDict = {"1": 100, "2": "lxc"}
print(nameDict["1"])
nameDict["3"]="haha"
nameDict["3"]="3000"
del nameDict["3"]
print(nameDict)


# set 无序不可重复的集合
# 通过列表或者字符串创建
# 交、并、差集 & | - 
set1=set('hello')
set2=(['h','e', 'n'])

print(set1)
set1.add("n")
set1.remove("h")
print(set1)


# 条件语句

#Python 程序语言指定任何非 0 和非空（null）、 非空字符串 值为 True，0 或者 null 为 False。
# 非空 list 等，判断为 True，否则为 False
# 不用大括号，if else下面的语句就是一个语句块;冒号和缩进是一种语法。它会帮助 Python 区分代码之间的层次，理解条件执行的逻辑及先后顺序。
# or （或）表示两个条件有一个成立时判断条件成功
# and （与）表示只有两个条件同时成立的情况下，判断条件才成功。
# 使用 range(x) 函数，就可以生成一个从 0 到 x-1 的整数序列。如果是 range(a,b) 函数，你可以生成了一个左闭右开的整数序列。
result=59
if result >= 60 :
    print("及格")
    print("==111111")
else :
    print("不及格")
    print("==")

num=0
if num :
    print("true")
else :
    print("false")

if num > 10:
    print("a")
elif num > 1:
    print("b")
else:
    print("c")

# 循环语句

for letter in 'Hello 两点水':
    print(letter)
dict11={"1":"a","2":"b"}
for i in dict11:
    print(i)

set={"11","aa", 100, 39}
for i in set:
    print(i)

list22=["11","aa", 100, 39]
for i in list22:
    print(i)

list22=(1,2, "aaa", 55.5)
for i in list22:
    print(i)

# 比如 range(0,10,2) , 它的意思是：从 0 数到 10（不取 10 ），每次间隔为 2 。
for i in range(1, 10, 2):
    print(i)

count=1
sum=0
while count <= 100:
    sum = sum + count
    count = count + 1
print(sum)

count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if ( sum > 5000):
        break
    count = count + 1
else:# 循环体执行完后执行else
    print(sum)
print(sum)

# 函数

# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
# 函数的第一行语句可以选择性地使用文档字符串（用于存放函数说明）
# 函数内容以冒号起始，并且缩进
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。
# 可以以元组方式返回多个值
# 默认参数的值是不可变的对象，比如None、True、False、数字或字符串;
# 只有在形参表末尾的那些参数可以有默认参数值， 如果存在可变参数，建议默认值参数放在可变参数前，否则必须通过关键字参数方式传值
# 在 Python 中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。
# 可变长参数也支持关键字参数（位置参数），即是在参数前边加 **
# 定义的函数希望某些参数强制使用关键字参数传递，这时候该怎么办呢？  将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果
# 调用时，关键字参数必须跟随在位置参数后面! 因为python函数在解析参数时, 是按照顺序来的, 位置参数是必须先满足, 才能考虑其他可变参数.
# 不可更改的类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是 a 的值，没有影响 a 对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可更改的类型：类似 c++ 的引用传递，如 列表，字典。如 fun（a），则是将 a 真正的传过去，修改后 fun 外部的 a 也会受影响
# 匿名函数，这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。所以建议还是遇到这种情况还是使用第一种解法。

def test(str1, obj):
    print(str1)
    print(obj)
    return None
test("124", ["a","c"])

def  division ( num1, num2 ):
	# 求商与余数
         a = num1 % num2
         b = (num1-a) / num2
         return b , a

num1 , num2 = division(9,4)
tuple1 = division(9,4)

print (num1,num2)
print (tuple1)


def print_user_info( name , age , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数

print_user_info( '两点水' , 18 , '女')
print_user_info( '三点水' , 25 )

def print_info( a , b = [] ):
    print(b)
    return b

result = print_info(1)
result.append('error')
print_info(2)

def print_user_info( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数

print_user_info( name = '两点水' ,age = 18 , sex = '女')
print_user_info( name = '两点水' ,sex = '女', age = 18 )

def print_user_info( name ,  age  , sex = '男' , ** hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return

# 调用 print_user_info 函数
print_user_info( '两点水' ,18 , '女')
print_user_info( name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))

def print_user_info( name , *a, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数
print_user_info( name = '两点水' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
print_user_info('两点水'  , '女' ,age=181)
print_user_info('两点水',age='22',sex='男')

num2 = 100
sum1 = lambda num1 : num1 + num2

num2 = 10000
sum2 = lambda num1 : num1 + num2

print( sum1( 1 ) )
print( sum2( 1 ) )


# 迭代器和生成器
# python中可迭代对象字符串、列表、元组、字典
# 迭代器，迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next(),且字符串，列表或元组对象都可用于创建迭代器，迭代器对象可以使用常规 for 语句进行遍历，也可以使用 next() 函数来遍历。


# 异同：迭代器通过已经存在的数据创建，而生成器不需要

# 1、字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter ( str1 )

# 2、list对象创建迭代器
list1 = [1,2,3,4]
iter2 = iter ( list1 )

# 3、tuple(元祖) 对象创建迭代器
tuple1 = ( 1,2,3,4 )
iter3 = iter ( tuple1 )

# for 循环遍历迭代器对象
for x in iter1 :
    print ( x , end = '' )

print('\n------------------------')

# next() 函数遍历迭代器
while True :
    try :
        print ( next ( iter3 ) )
    except StopIteration :
        print("异常")
        break

print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

# list 生成式
list1=list(range(1,31))
print(list1)


list1=[x * x for x in range(1, 11)]
print(list1)

list1= [x * x for x in range(1, 11) if x % 2 == 0]
print(list1)

list1= [(x+1,y+1) for x in range(3) for y in range(5)]
print(list1)


# 在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。并在下一次执行 next()方法时从当前位置继续运行。
# 生成器可以看做一种特殊的迭代器
# 函数式生成器可重复调用执行
gen= (x * x for x in range(10))
for num  in  gen :
    print(num)

# -*- coding: UTF-8 -*-
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
# 引用函数
for x in fibon(10):
    print(x , end = ' ')

# 为了同时迭代多个序列，使用 zip() 函数，迭代次数一最短序列为准，zip可接受多个序列，且能创建字典对象

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19]
for name, age in zip(names, ages):
    print(name,age)

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19]

dict1=dict(zip(names,ages)) # dict不可前面被定义，否则此处无效

print(dict1)


# 正则
# 贪婪模式：它的特性是一次性地读入整个字符串，如果不匹配就吐掉最右边的一个字符再匹配，直到找到匹配的字符串或字符串的长度为 0 为止。
# 它的宗旨是读尽可能多的字符，所以当读到第一个匹配时就立刻返回。

# 懒惰模式：它的特性是从字符串的左边开始，试图不读入字符串中的字符进行匹配，失败，则多读一个字符，再匹配，如此循环，
# 当找到一个匹配时会返回该匹配的字符串，然后再次进行匹配直到字符串结束。

import re

a = 'java*&39android##@@python'

# 数量词
findall = re.findall('[a-z]{4,7}', a)
print("贪婪模式：", findall)

re_findall = re.findall('[a-z]{4,7}?', a)
print("懒惰模式：", re_findall)

print("1：", re.findall('\A(.*?)\Z', a))