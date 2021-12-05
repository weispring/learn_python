print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

# list 生成式
list1=list(range(1,31))
print(list1)

# 杨辉三角

# join

def triangles( n ):         # 杨辉三角形
    L = [1]
    while True:
        print("==", L)
        yield L
        L.append(0)
        print(">>>", L)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]

n= 0
for t in triangles( 10 ):   #直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break

# 调用class.a=""，无法覆盖对象的属性值
# 如何销毁对象

if __name__ == '__main__':
    print("")

#对象的描述器
# __metaclass__

# 经常运行报错

import module1

