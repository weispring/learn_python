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