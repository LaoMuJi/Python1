def set_func(func):
    def call_func(a):
        func(a)
    return call_func


# 装饰器有不同的内存空间
# 先执行装饰器，然后装饰器调用func(a)来执行test，func = test()。
# 装饰器加载时候就执行了，不是调用才执行
@set_func
def test(num):
    print(num)

test(100)
# 等于 XX = set_func(test)







# 通用装饰器加return返回
def set_func1(func):
    def call_func(*args, **kwargs):
        # 拆包
        return func(*args, **kwargs)
    return call_func


@set_func1
def test1(num, *args, **kwargs):
    print(num,args,kwargs)
    return 'ok'

a = test1(100)
b = test1(100, 200, 300)
c = test1(100, 200, 300, z=100, x=200, c=300)
print(a)







# 两个装饰器
def set_func_2(func):
    def call_func():
        return '<h1>' + func() + '</h1>'
    return call_func

def set_func_3(func):
    def call_func():
        return '<td>' + func() + '<td>'
    return call_func

@set_func_2
@set_func_3
def get_str():
    return '哈哈'

print(get_str())






# 类装饰器
class abc(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('添加功能')
        return self.func()

@abc
def aaa():
    return 'hahaha'

print(aaa())







#带有参数的装饰器
def set_level(level_num):
    def set_func4(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                            print("----权限级别1，验证----")
            elif level_num == 2:
                print("----权限级别2，验证----")
            return func()
        return call_func
    return set_func4

# 1. 调用set_level函数，把1当做实参
# 2. set_level返回一个装饰器的引用，即set_func
# 3. 用返回的set_func对test1函数进行装饰（装饰过程与之前一样）
@set_level(1)
def test1():
        print("-----test1---")
        return "ok"

@set_level(2)
def test2():
    print("-----test2---")
    return "ok"

test1()
test2()















# 类方法
@classmethod
def abc(cls):
    print("2")



# 静态方法，不需要传递参数
@staticmethod
def bcd():
    print("3")


