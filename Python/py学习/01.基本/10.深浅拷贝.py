import copy
a = 9

# 浅拷贝 只复制当前对象
# 不复制二级、不能拷贝元祖
# 不能字典里面值是对象
b = copy.copy(a)


# 深拷贝、有指向元祖可以拷贝
c = copy.deepcopy(a)

