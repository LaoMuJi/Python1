def test1():
    a=2
    def test2():
        # 装饰器里面变量用nonlocal
        nonlocal a
        print(a)
        a=3
        print(a)

    # test2() 括号表示返回这函数返回值
    return test2

a = 1

t=test1()
t()