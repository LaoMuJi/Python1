import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        print('开始', nloop, '时间', ctime())
        sleep(nsec)
        print('完成', nloop, '时间', ctime())

def hehe():
    print(00000)


def main():
    print("开始时间", ctime())

    t1 = threading.Thread( target = ThreadFunc('loop').loop, args=("一", 6))
    t2 = threading.Thread( target = ThreadFunc('loop').loop, args=("二", 4))

    # 3秒后执行hehe
    t3 = threading.Timer(3, hehe)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("结束时间", ctime())

if __name__ == '__main__':
    main()