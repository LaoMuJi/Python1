# lambda 表达式
stm2 = lambda x,y,z: x+ y*10 + z*100
print(stm2(4,5,6))


# map 把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
# map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
l1 = [i for i in range(10)]

def jisuan(n):
    return n*10

l2 = map(jisuan,l1)

for i in l2:
    print(i)

print()



# reduce 把一个可迭代对象合并成一个结果

from functools import reduce

# 相加操作
def myAdd(x, y):
    return x + y

# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd, [1, 2, 3, 4, 5, 6])
print(rst)


