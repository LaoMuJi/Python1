# import collections
from time import sleep

class Class1(object):
    def __init__(self):
        self.name = []
        self.num = 0

    def add(self, name):
        self.name.append(name)

    # 有iter称为迭代对象
    def __iter__(self):
        return self

    # 有iter、next称为迭代器
    def __next__(self):
        ret = self.name[self.num]
        self.num += 1
        return ret


a = Class1()

a.add('1')
a.add('2')
a.add('3')
a.add('4')



# # 是否可以迭代的对象
# print(isinstance(a,collections.Iterable))
# b = iter(a)
#
# # 是否是迭代器
# print(isinstance(b,collections.Iterator))
#
# print(next(b))


# raise StopIteration
for c in a:
    sleep(1)
    print(c)
