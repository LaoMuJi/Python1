import time
import threading

def loop1(in1):
    print(in1)
    time.sleep(4)
    print('1结束')

def loop2(in1, in2):
    print(in1, in2)
    time.sleep(2)
    print('2结束')


def main():
    print("开始")
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("参数",))
    # setName是给每一个子线程设置一个名字
    t1.setName("名字1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=("参数1", "参数2"))
    t2.setName("名字2")
    t2.start()

    # join子线程结束主线程才结束
    # t1.join()
    # t2.join()
    time.sleep(1)





    for thr in threading.enumerate():
        # getName能够得到线程的名字
        print("正在运行的线程名字是： {0}".format(thr.getName()))

    print("正在运行的子线程数量为： {0}".format(threading.activeCount()))
    print("结束")


if __name__ == "__main__":
    main()
