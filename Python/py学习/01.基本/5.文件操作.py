# r     以只读方式打开文件。默认方式。文件不存在报错
#
# w     以只写方式打开文件。文件存在会覆盖，不存在创建新文件
#
# x     创建方式打开，如文件已经存在，报错
#
# a     以追加方式打开文件。不存在创建新文件
#
# b     binary方式，二进制方式写入
#
# r+    以读写方式打开文件。文件指针在开头。文件不存在报错
#
# w+    以读写方式打开文件。文件存在会覆盖，不存在创建新文件
#
# a+    以读写方式打开文件。文件存在，追加。文件不存在，创建新文件
#
# +     可读写


with open(r'ZZ0.txt', 'r', encoding='utf-8') as f:   # r表示后面字符串内容不需要转义

    # 按行读取内容
    strline = f.readline()
    print(strline)

    # 把文件内每一行内容作为一个元素
    l = list(f)
    print(l)

    # 打开文件后，从第N个字节出开始读取
    #     0： 从文件头开始偏移
    #     1：从文件当前位置开始偏移
    #     2： 从文件末尾开始偏移
    f.seek(4058, 0)

    # 用来显示文件读写指针的当前位置
    pos = f.tell()
    print(pos)

    # read是按字符读取文件内容
    strChar = f.read(1)
    print(strChar)


# 写文件
with open(r'ZZ1.txt', 'w+', encoding='utf-8') as f:      # a代表追加方式打开

    f.write("平日里刺耳的父亲的话语\n今天却倍感温暖\n")

    # 写入行
    f.writelines("我只是跟随着你 做你的影子\n")
    f.writelines("只要一点点时间就好 再给我一点点时间就好\n")

    # 写入列表
    f.writelines(l[1])



# 持久化

# 序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
import pickle

age = 19
a = [19, [185, 76]]

# 序列化案例
with open(r'ZZ2.txt', 'wb') as f:
    pickle.dump(age, f)

# 反序列化案例
with open(r'ZZ2.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)
    print(a)



# db数据 类似字典，用kv对保存数据，存取方式跟字典也类似
# 不支持多个应用并行写入，open的时候可以使用flag=r(文件不存在报错)
import shelve

# 保存
with shelve.open(r'ZZ3.db', writeback=True) as shv:
    shv['one'] = "这是1"
    shv['two'] = 2
    shv['three'] = 3

# 读取
with shelve.open(r'ZZ3.db') as shv:
    print(shv['one'])