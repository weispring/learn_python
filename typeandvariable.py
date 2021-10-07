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
dict={"1":"a","2":"b"}
for i in dict:
    print(i)

set={"11","aa", 100, 39}
for i in set:
    print(i)

list=["11","aa", 100, 39]
for i in list:
    print(i)

list=(1,2, "aaa", 55.5)
for i in list:
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