# 私有属性
class X(object):

    # 首先执行
    def __init__(self, num):
        # 私有变量
        self.num = num
        self.__b = "我是b变量"
        # print(self.__b)

    # 私有属性
    def __siyou(self):
        self.a = 1
        print(self.a, self.num)

    # args是元祖，多余的参数会传入，变成元祖
    # kwargs是字典、a=1会传入
    def abc(self, *args, **kwargs):
        print(args)
        print(kwargs)



class Y(X):

    def de(self):
        # 调用子
        self.abc()
        # super()代表得到父类
        super().abc
        print('干活中2')


# 私有
x = X('99')
print(x._X__b)  # 我是b变量
x._X__siyou()  # 1, 99


# 调用子
y = Y('99')
y.de()  # 干活中 干活中1 干活中2




# 私有属性或方法 import无法导入，类、之类可以访问
_a = 4
# print(a)


print('*'*10)
X.abc(1,2,3, m=10, n=11)