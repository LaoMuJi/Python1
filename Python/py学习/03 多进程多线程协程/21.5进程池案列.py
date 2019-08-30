import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + '/' + file_name, 'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + '/' + file_name, 'wb')
    new_f.write(content)
    new_f.close()
    q.put(file_name)


if __name__ == '__main__':
    old_folder_name = input('请输入')

    try:
        new_folder_name = old_folder_name + '复制'
        os.mkdir(new_folder_name)
    except:
        pass

    file_names = os.listdir(old_folder_name)

    po = multiprocessing.Pool(5)

    q = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    file_num = len(file_names)
    copy_num = 0

    while True:
        file_name = q.get()
        copy_num += 1
        print('\r进度为%.0f%%' % (copy_num*100/file_num), end='')

        if copy_num >= file_num:
            break
    print()
