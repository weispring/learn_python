- 作用域

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。