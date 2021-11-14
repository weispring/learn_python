
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


a = 'Python*Android*Java-888'

# 把字符串中的 * 字符替换成 & 字符
sub1 = re.sub('\*', '&', a)
print(sub1)

# 把字符串中的第一个 * 字符替换成 & 字符
sub2 = re.sub('\*', '&', a, 1)
print(sub2)


# 把字符串中的 * 字符替换成 & 字符,把字符 - 换成 |

# 1、先定义一个函数
def convert(value):
    group = value.group()
    if (group == '*'):
        return '&'
    elif (group == '-'):
        return '|'


# 第二个参数，要替换的字符可以为一个函数
sub3 = re.sub('[\*-]', convert, a)
print(sub3)


a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'

# 使用 re.search
search = re.search('<img src="(.*)">', a)
# group(0) 是一个完整的分组
print(search.group(0))
print(search.group(1))

# 使用 re.findall
findall = re.findall('<img src="(.*)">', a)
print(findall)

# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)
# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())
print(re.match('<img src="(.*)">', a).groups(1))