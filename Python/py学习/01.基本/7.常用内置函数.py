import math

# 向上取整数
print(math.ceil(5.01))

# 向下取整数
print(math.floor(5.01))


# 查看喜欢保留关键字
import keyword
print(keyword.kwlist)


# 四舍五入
print(round(5.5))


# 开平方
print(math.sqrt(6))

# 幂运算，第一个是底数，第二个是指数
print(math.pow(4,3))  # 4的3次方 返回浮点数
print(4**3)  # 返回整数

# 对一个数值获取它的绝对值，返回浮点数
print(math.fabs(-99))
print(abs(-99))  # 获取绝对值操作，py内置函数，返回

# 求和
print(math.fsum([1,4,5,7]))  # 返回浮点数
print(sum([1,4,5,7]))  # 内置函数

# 将一个浮点数拆分为整数部分和小数部分，返回元祖
print(math.modf(1.22))

# 将第二个数的符号传给第一个数
print(math.copysign(-1,2))


