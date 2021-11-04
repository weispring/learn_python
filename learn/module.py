# 在模块中，我们不但可以直接存放变量，还能存放函数，还能存放类。
# 在 Python 中，一个 .py 文件就称之为一个模块（Module）。
# 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突。
# 引入模块 import module1[, module2[,... moduleN]， from modname import name1[, name2[, ... nameN]]
# 引入了包，这样子做就算有相同的模块名，也不会造成重复，因为包名不同，其实也就是路径不同。

if __name__=='__main__':
    print("main")
else:
    print("not main")

# 在 Python 中，所有以 "__" 双下划线包起来的方法，都统称为"魔术方法"。比如我们接触最多的 __init__ 。
# 我们可以使用 Python 内置的方法 dir() 来列出类中所有的魔术方法.示例如下：
class User(object):
    pass
print(dir(User()))

# __new__ 是用来创建类并返回这个类的实例, 而__init__ 只是将传入的参数来初始化该实例.__new__ 在创建一个实例的过程中必定会被调用,但 __init__ 就不一定，比如通过 pickle.load 的方式反序列化一个实例时就不会调用 __init__ 方法。
# def __new__(cls) 是在 def __init__(self) 方法之前调用的，作用是返回一个实例对象。还有一点需要注意的是：__new__ 方法总是需要返回该类的一个实例，而 __init__ 不能返回除了 None 的任何值
class User2(object):
    def __new__(cls, n, v):
        print("new", n, v)
        return super(User2, cls).__new__(cls) #调用父类构造才会执行下面的初始化方法

    def __init__(self, name, code):
        print("init")
        self.name=name
        self.code=code

print(User2('n', 'c'))


# Python 其实可以通过魔术方法来实现封装。

class FunctionalList:
    ''' 实现了内置类型list的功能,并丰富了一些其他方法: head, tail, init, last, drop, take'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 获取第一个元素
        return self.values[0]

    def tail(self):
        # 获取第一个元素之后的所有元素
        return self.values[1:]

    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]

    def last(self):
        # 获取最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 获取所有元素，除了前N个
        return self.values[n:]

    def take(self, n):
        # 获取前N个元素
        return self.values[:n]



v1=FunctionalList(["22", "哈哈哈"])
for x in v1:
    print(v1.__getitem__(1))

# 枚举
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 遍历枚举类型,而且 Enum 的成员均为单例（Singleton），并且不可实例化，不可更改
for  member in Month.__members__.items():
    print(member[0],",", member[1],",", member[1].value, '----------', member)
# 直接引用一个常,量
print('\n', Month.Jan)
print('\n', Month.Jan.name)
print('\n', Month.Jan.value)

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month1(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'
for name, member in Month1.__members__.items():
        print(name, '----------', member, '----------', member.value)

# 也就是 Enum 类的枚举是不支持大小运算符的比较的。使用 IntEnum 类进行枚举，就支持比较功能。
from enum import IntEnum
class User3(IntEnum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12
try:
    print('\n'.join(s.name for s in sorted(User3)))
except TypeError as err:
    print(' Error : {}'.format(err))


# Python 中类也是对象
# 因为只要使用关键字 class ，Python 解释器在执行的时候就会创建一个对象。
# 当程序运行这段代码的时候，就会在内存中创建一个对象，名字就是ObjectCreator。这个对象（类）自身拥有创建对象（类实例）的能力

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
# 可以看到，在 Python 中，类也是对象，你可以动态的创建类。
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

def printHello(self, name="py"):
    print('printHello,', name)


Hello=type('Hello', (object,), dict(hello=printHello))
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

# 元类
# 你也可以理解为，元类就是负责生成类的。
# 而 type 就是内建的元类。也就是 Python 自带的元类。实际上 type() 函数是一个元类。
# 你可以通过检查 __class__ 属性来看到这一点。Python 中所有的东西，注意喔，这里是说所有的东西，他们都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来。

age=23
name="两点水"
def fu():
    pass
class eat(object):
    pass
mEat=eat()

print(age.__class__)
print(name.__class__)
print(fu.__class__)
print(mEat.__class__)
print(age.__class__.__class__)
print(name.__class__.__class__)
print(fu.__class__.__class__)
print(mEat.__class__.__class__)

import sys
print(sys.version)