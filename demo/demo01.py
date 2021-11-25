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