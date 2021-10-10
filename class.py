# 类定义，调用，修改

class ClassTest:
    var1=100
    var2="1"
    va3=[1]

    #@classmthod 类方法会带有自身这个参数，不需要用户传入
    def method1(cl, v1):
        print("method1",cl.var1, v1)
    def method2(v1):
        print("method2", v1)
    def set1(v1):
        ClassTest.var1=v1

print(ClassTest.method1(ClassTest, "1"))
ClassTest.set1(10000000000) # 如何改变类的属性值
ClassTest.var1=1009
print(ClassTest.var1)
print(ClassTest.method2("2"))
ClassTest.var100="add"
print(ClassTest.var100)

# 类实例化
# 类方法里面没有了 @classmethod 声明了，不用声明他是类方法
# 类方法里面的参数 cls 改为 self
# 类的使用，变成了先通过 实例名 = 类() 的方式实例化对象，为类创建一个实例，然后再使用 实例名.函数() 的方式调用对应的方法 ，使用 实例名.变量名 的方法调用类的属性

class ClassA(object):
    def __init__(self): #函数就是初始化函数，也叫构造函数。可加参数
        print("构造函数")
    def __del__(self):
        print("销毁对象")
    var1=100
    var2="test"

    def method1(self):
        print(self.var2)
    def set2(self, v2):
        self.var2=v2

a=ClassA()
def method1c(self):
    print("method1 changed")
ClassA.method1=method1c
a.method1()
a.set2("test_modify")
# a.var2="test_modify_11"
# ClassA.var2="9000" # 这行能够让下面的两个对象的输出属性值发生变化，但是如果在前面加了set2这行，对a对象不起作用？
print("===", a.var2)
a.method1()


b=ClassA()
b.method1()
print("===", b.var2)


# 类可多继承
# 若是父类中有相同的方法名，而在子类使用时未指定，python 在圆括号中父类的顺序，从左至右搜索 ， 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
# 调用父类方法、重写父类方法、判断类型

class P(object):
    var1=100
    def testmethod(self):
        print("p")

class P1():
    var1=100
    def testmethod(self):
        print("p1")

class P2(P,P1):
    var1=100
    def testmethod1(self):
        #super().testmethod() #知道第一个类执行
        super(P1, self).testmethod()  # 多继承，执行指定父类
        print("p2")

po=P2()
print(isinstance(po, P))
print(isinstance(po, P1))
po.testmethod1()


