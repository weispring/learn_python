# 首先判断 Foo 中是否有 __metaclass__ 这个属性？如果有，Python 会在内存中通过 __metaclass__ 创建一个名字为 Foo 的类对象（注意，这里是类对象）。如果 Python 没有找到__metaclass__ ，它会继续在 Bar（父类）中寻找__metaclass__ 属性，并尝试做和前面同样的操作。如果 Python在任何父类中都找不到 __metaclass__ ，它就会在模块层次中去寻找 __metaclass__ ，并尝试做同样的操作。如果还是找不到 __metaclass__ ,Python 就会用内置的 type 来创建这个类对象。
# 元类的主要目的就是为了当创建类时能够自动地改变类。

def upper_attr(cls, cls_parents, attrs):
    # 将属性转换为大写
    attrs=((name, value)for name, value in attrs.items() if not name.startwith("__"))
    uppercase_attr=dict((name.upper(),value) for name, value in attrs)
    return type.__new__(cls, cls_parents, uppercase_attr)

__metaclass__=upper_attr

class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Foo(object):
    __metaclass__=UpperAttrMetaclass
    bar="bip"
    var=100

f=Foo()
print(f.bar)

