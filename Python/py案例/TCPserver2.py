import time
import socket
import gevent


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 服务器先关闭保证端口立即关闭不会被占用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #设置套接字为非堵塞方式
    tcp_server_socket.setblocking(False)
    # 绑定本地信息
    tcp_server_socket.bind(('', 8888))

    # 让默认的套接字为坚定
    tcp_server_socket.listen(128)

    client_socket_list = []
    while True:
        # time.sleep(0.5)
        try:
            # 等待客户端的链接
            new_client_socket, client_addr = tcp_server_socket.accept()
            print(client_addr)
        except Exception as ret:
            # print('等待连接')
            pass
        else:

            new_client_socket.setblocking(False)
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
                print(recv_data.decode())
            except Exception as ret:
                print('无数据')
                pass
            else:
                if recv_data:
                    # 对方发送来的数据

                    # 返回消息
                    client_socket.send('已收到'.encode())
                else:
                    client_socket_list.remove(client_socket)
                    # 关闭套接字
                    client_socket.close()
                    print('对方已关闭')

    tcp_server_socket.close()


if __name__ == '__main__':
    main()