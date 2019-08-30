import multiprocessing
import time


def worker(msg):
    time.sleep(5)
    print(msg, '执行完毕')


if __name__ == '__main__':  # 必须有

    po = multiprocessing.Pool(5)  # 定义一个进程池 最大
    for i in range(0, 100):
        po.apply_async(worker, (i,))

    print('开始')
    po.close()  # 关闭进程池，关闭后po不再接受新的请求
    po.join()  # 等待po中所有子进程执行完毕，必须放在close后
    print('结束')
