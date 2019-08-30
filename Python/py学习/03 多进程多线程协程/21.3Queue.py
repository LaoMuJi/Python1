import multiprocessing
import time


def downz(q):
    # 模拟数据
    data1 = [1,2,3,4,5,6,7,8,9,0]

    for i in range(100000,100010):
        q.put(i)


def dataz(q):
    data2 = []
    # 从列队获取数据
    while True:
        # q数量
        print(q.qsize())

        d = q.get()
        data2.append(d)

        # 判断Q是否为空 q.full() 满
        if q.empty():
            break
    print(data2)


def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=downz, args=(q,))
    p2 = multiprocessing.Process(target=dataz, args=(q,))
    p1.start()
    # time.sleep(0.1)
    p2.start()


if __name__ == '__main__':
    main()