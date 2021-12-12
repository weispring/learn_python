
x = 100
print(eval( '3 * x' ))
exec ("""
for i in range(5):
    print ("iter time: %d" % i)
    """)

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    exec(expr, {'x': 1, 'y': 2, 'z': 3}, {'x': 10, 'y': 22, 'z': 80})

# 内部变量z无法改变，外边变量loca优先级与global
func()

print("ord('a') : {}, chr(97): {}".format(ord('a'), chr(97)))

def is_odd(n):
    return n % 2 == 1

tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

for i in  bytes([1,2,3,4]):
    print(i)

print( "{1} {0} {1}".format("hello", "world"))


class C(object):
    def __init__(self):
        self.__x = None

    def getx(self):
        print("getx 被调用")
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx,  "I'm the 'x' property.")

print(C().x)

print(vars(C()))
print(locals())
print( globals())