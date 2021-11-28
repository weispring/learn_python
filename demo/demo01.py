print("111", "22")

'''
多行注释
'''
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
print("第一行",\
"第二行")

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
#Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
a = "123";print(a)
print(a * 2)             # 输出字符串两次
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


'''
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True
'''
# 您可以通过使用del语句删除单个或多个对象
a = 111
print(isinstance(a, int))
print(a)
'''
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''

print(True==1)

print("除法，得到一个浮点数",2 / 4)  #

print("除法，得到一个整数", 9 // 4) #
print("取余", 17 % 3) # 取余
print("乘方", 2 ** 5) # 乘方

'''
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''



list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print(list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
tinylist.append("11")
testlist = tinylist[0:2]
testlist[1] = "test"
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

def reverseWords(input):
        # 通过空格将字符串分隔符，把各个单词分隔为列表
        inputWords = [1,2,3,4]

        # 翻转字符串
        # 假设列表 list = [1,2,3,4],
        # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
        # inputWords[-1::-1] 有三个参数
        # 第一个参数 -1 表示最后一个元素
        # 第二个参数为空，表示移动到列表末尾
        # 第三个参数为步长，-1 表示逆向
        inputWords=inputWords[-1::-1]

        # 重新组合字符串
        return inputWords

if __name__ == "__main__":
        input = 'I like runoob'
        rw = reverseWords(input)
        print(rw)


'''
元组写在小括号 () 里，元素之间用逗号隔开。元组中的元素类型也可以不相同

、与字符串一样，元组的元素不能修改,元素可以是可变的对象，list
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
tup3 = (1, 23, "换货", ["1","2"])
print(tup3)
tup3[3][0]="11"
print(tup3)


'''
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
        print('Runoob 在集合中')
else :
        print('Runoob 不在集合中')
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])

# set可以进行集合运算
a = {'a','b','c'}
b = {'a','d','e'}

print("差集：", a - b)     # a 和 b 的差集

print("并集", a | b)     # a 和 b 的并集

print("交集", a & b)     # a 和 b 的交集

print("==", a ^ b)     # a 和 b 中不同时存在的元素


'''

'''

dic = {}
dic['one'] = "1 - 菜鸟教程"
dic[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dic['one'])       # 输出键为 'one' 的值
print (dic[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值


# 字典的创建方式
dic = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dic)
print({x: x**2 for x in (2, 4, 6)})
print(dict(Runoob=1, Google=2, Taobao=3))

tup1 = ("1", 1)
tup2 = ("2", 222)
print("测试构建字典：", dict([tup1, tup2]))

'''
:=	海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
'''


# 在这个示例中，赋值表达式可以避免调用 len() 两次:
# 打印前加f是为了格式化输出n的值
a = "1233"
if (n := len(a)) > 2:
        print(f"List is too long ({n} elements, expected <= 10)")

a = False;
b = True;
if(a and b):
        print("if")
else:
        print("else")

if(a or b):
        print("if")
else:
        print("else")


a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
        print ("1 - 变量 a 在给定的列表中 list 中")
else:
        print ("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
        print ("2 - 变量 b 不在给定的列表中 list 中")
else:
        print ("2 - 变量 b 在给定的列表中 list 中")


'''
身份运算符用于比较两个对象的存储单元
is 
is not 
id() 函数用于获取对象内存地址。
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''

a = 20
b = 20

if ( a is b ):
        print ("1 - a 和 b 有相同的标识")
else:
        print ("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
        print ("2 - a 和 b 有相同的标识")
else:
        print ("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if ( a is b ):
        print ("3 - a 和 b 有相同的标识")
else:
        print ("3 - a 和 b 没有相同的标识")

if ( a is not b ):
        print ("4 - a 和 b 没有相同的标识")
else:
        print ("4 - a 和 b 有相同的标识")


'''
深浅拷贝
'''

a = [1,2,8]
print(id(a))
print(id(a[:]))
b = a[:] # 深拷贝
print(id(b))


# 常见数据类型
'''
Python 数字数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。如int(a)
// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
数字函数
随机数函数
三角函数
pi e
'''
import random
import math
print("16进制", 0x1F, "八进制", 0o37)
print(5//2, 5.0//2)
a = [1,2,200,5]
print(min(a), max(a))
print(random.choice(range(10)))
print(random.randrange(1, 100, 10), random.random(), random.seed(100), random.uniform(10.1, 10.2))
print(math.pi, math.e)



'''
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：
变量[头下标:尾下标]

转义字符
r/R	原始字符串
格式化输出,f-string 格式化字符串更方便
三引号 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去。
在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：

字符串函数
'''


print("Hello\tWorld!", "Hello \t          World!")
print('\a')
print("Hello\bWorld!")
print( r'\n' )
a = ('小明', 10, 11.112)
print ("我叫 %s 今年 %d 岁! %u" % a)
print("格式化：%s" % "ddd")

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB (\t)。''
也可以使用换行符 [\n]。
"""
print (para_str)

name = "姓名"
print(f"hahh,{name}")
x = 1
print(f"结果是：{x+1}")
print(f'{x+1=}')
x = "name"
name1 = "重复查找"
print(f"结果是：{x+str(1)}")
a= {"1": "hahh"}
print(f'{a["1"]}')
print("ss".center(10, "1"))

# 存在
a = "哈哈哈12389uuxl"
if(a.find("uu") > -1):
        print(a.find("uu")) # 用find不用index,因为index方法不存在会抛出异常

# 替换
print("12hh雨衣".replace("12", "oo"))
# 大小写转换
print("hhhyyXX".upper())
