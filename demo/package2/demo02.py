# 迭代器和生成器

''''
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。


在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
'''
import sys

# 自定义包需要在path中加入路径
sys.path.append("D:\\learn_code\\learn_python")


from demo.package1 import constant

lis = [1,2,3,5]
ite = iter(lis)
for x in ite:
        print(x, end="\n")
ite = iter(lis)
while True:
        try:
                print (next(ite))
        except StopIteration:
                print("迭代结束")
                break


class MyNumbers:
        def __iter__(self):
                self.a = 1
                return self

        def __next__(self):
                if self.a <= 20:
                        x = self.a
                        self.a += 1
                        return x
                else:
                        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
        try:
                print(x)
        except StopIteration:
                print("哈哈自定义迭代类迭代结束")
                break

# 函数
'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响


以下是调用函数时可使用的正式参数类型：
必需参数
关键字参数
默认参数
不定长参数
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
加了两个星号 ** 的参数会以字典的形式导入。
如果单独出现星号 * 后的参数必须用关键字传入。
'''
def test1(*param):
        for x in param:
                print(x)

test1("122", 100, 999)

def test2(**param):
        for x in param.items():
                print(x)
        for x in param.keys():
                print(param[x])

test2(a=100,b=200,c="hh")

def test1(p,*, hh):
        print(p, hh)

test1("122", hh="哈哈")

# 匿名函数
'''
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

# 强制位置参数
'''
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
'''

def f(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)

'''
list 可做栈使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
这里我们将列表中每个数值乘三，获得一个新的列表

遍历技巧

'''

lis = [1,2,100]
print(lis[3:])
lis[len(lis):]=["hhh"]
print(lis)
vec = [1,2,3]
vec1 = [3*x for x in vec if x <= 3]
print(vec1)
# 删除数组元素
del vec1[1:2]

a = {x: x**2 for x in (2, 4, 6)}
print(a)

for k,v in a.items():
        print(k,v)
for i,v in enumerate(["aa","bcc","cd"]):
        print(i, v)
#同时遍历两个序列
a = [1,2,3]
b= ["dd", 'rr']
for m, n in zip(a, b):
        print('a:{0}, b: {1}'.format(m,n))


# 模块
'''
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量

模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。
所以，模块的作者可以放心大胆的在模块内部使用这些全局变量，而不用担心把其他用户的全局变量搞混。
从另一个方面，当你确实知道你在做什么的话，你也可以通过 modname.itemname 这样的表示法来访问模块内的函数。
模块是可以导入其他模块的。在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，当然这只是一个惯例，而不是强制的。被导入的模块的名称将被放入当前操作的模块的符号表中。

from fibo import fib, fib2
这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，fibo 这个名称是没有定义的）。

这还有一种方法，可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表:
from fibo import *
这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。

dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为 __all__变量赋值。
注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包
'''

import sys

print('命令行参数如下:')
for i in sys.argv:
        print(i)

print('\n\nPython 路径为：', sys.path, '\n')


print(dir())

print(constant.aa)

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]}; Taobao: {0[Taobao]:d}'.format(table))

str = input("请输入：");
print ("你输入的内容是: ", str)



f = open("foo.txt", "w", encoding="utf-8")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.close()
print(open("foo.txt", encoding="utf-8").read())
print(open("foo.txt", encoding="utf-8").readline())
# 关闭打开的文件
f = open("foo.txt", "r", encoding="utf-8")
for line in f:
        print(line, end='')


import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
output = open('data.pkl', 'wb')
pickle.dump(data1, output)
output.flush()
data2 = pickle.load(open('data.pkl', 'rb'))
print(data2)


''''
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
'''

for arg in sys.argv:
        try:
                f = open(arg, 'r', encoding="utf-8")
        except IOError:
                print('cannot open', arg)
        else:
                print(arg, 'has', len(f.readlines()), 'lines')
                f.close()
        finally:
                print('这句话，无论异常是否发生都会执行。')

def raiseexception():
        x = 10
        if x > 5:
                raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

try:
        raiseexception()
except:
        print("exception ")


# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

with open("foo.txt", encoding="utf-8") as f:
        for line in f:
                print(line, end="")
# 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。

'''
类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。

类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

多继承，需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值

'''

class MyClass:
        def __init__(self, a, b):
                self.a = a
                self.__b = b # 私有属性
                print(f"变量值为：{self.a}, {self.__b}")


a = MyClass("aaa", 300)
print(a.a, a.__setattr__("a", "哈哈哈"))
print(a.a)


class Parent:        # 定义父类
        def myMethod(self):
                print ('调用父类方法')

class Child(Parent): # 定义子类
        def myMethod(self):
                print ('调用子类方法')

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child, c).myMethod() #用子类对象调用父类已被覆盖的方法


'''
命名空间
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

有四种作用域：
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
规则顺序： L –> E –> G –> B。

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

'''

if True:
        msg_inner = "哈哈哈哈，我测试"
print(msg_inner)

def test():
        msg_inn = 'I am from Runoob'


# lobal 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

num = 1
def fun1():
        global num  # 需要使用 global 关键字声明
        print(num)
        num = 123
        print(num)
fun1()
print(num)


def outer():
        num = 10
        def inner():
                nonlocal num   # nonlocal关键字声明
                num = 100
                print(num)
        inner()
        print(num)
outer()


