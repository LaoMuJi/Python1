def num(num1):
    a, b = 0, 1
    num = 0
    while num < num1:
        # 如果有yield，不是函数，是一个生成器的模板
        c = yield a
        a, b = b, a+b
        num += 1
    return 'OK'


obj = num(100)

# 使用send参数赋予给 c 变量
# d = obj.send('111')
# print(d)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as e:
        print(e.value)
        break