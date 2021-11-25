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