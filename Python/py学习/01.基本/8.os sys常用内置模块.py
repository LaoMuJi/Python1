import os

# 查看当前路径
mydir = os.getcwd()
print(mydir)


# 改变当前目录
os.chdir('c:/')
mydir = os.getcwd()
print(mydir)


# 获取当前目录下所有文件、文件夹
ld = os.listdir()
print(ld)

# 执行命令行命令
rst = os.system("dir")
print(rst)

print(os.name)





import shutil

# 复制文件      (来源路径，目标路径)copy2
a = shutil.copy("/home/1.txt", "/home/2.txt")
print(a)

# 复制文件夹
a = shutil.copyfile("111", "222")

# 移动文件夹/文件
rst  = shutil.move("/home/1", "/home/2")

# 删除文件
os.remove('/home/1.txt')

# 删除文件夹 不为空报错
os.rmdir("/home/1")

# 递归 删除文件夹 子文件夹不为空报错
os.removedirs("/test")

# 重命名文件夹/文件 (来源路径，目标路径)
os.rename('1.txt', 'C:/Users/lcc92/Desktop/2.txt')

# 递归 重命名文件夹/文件 (来源路径，目标路径)
os.renames("1.txt","newdir/aanew.txt")



import zipfile

# 创建一个压缩包
# 默认值为’r’，表示读已经存在的zip文件     也可以为’w’或’a’
# ’w’表示新建一个zip文档或覆盖一个已经存在的zip文档
# ’a’表示将数据附加到一个现存的zip文档中。

with zipfile.ZipFile('C:/Users/lcc92/Desktop/test.zip', mode='w') as z:
    z.write('C:/Users/lcc92/Desktop/1.txt',compress_type=zipfile.ZIP_LZMA)
    z.write('C:/Users/lcc92/Desktop/0.jpg',compress_type=zipfile.ZIP_LZMA)


    # 获取zip包信息
    z1 = z.getinfo("1.zip")
    print(z)

    # 获取包所有文件名称列表
    z1 = z.namelist()
    print(z1)

    # 解压zip     参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称。
    z1 = z.extractall('C:/Users/lcc92/Desktop')


# 重新加载模块a
from importlib import reload
reload(a)