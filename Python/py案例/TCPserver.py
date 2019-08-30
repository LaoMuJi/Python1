import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 服务器先关闭保证端口立即关闭不会被占用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定本地信息
    tcp_server_socket.bind(('', 8888))

    # 让默认的套接字为坚定
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的链接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)

        while True:
            # 接收客服端发来的请求
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode())

            if recv_data:
            # 返回消息
                new_client_socket.send('已收到'.encode())
            else:
                break

        # 关闭套接字
        new_client_socket.close()
        break

    tcp_server_socket.close()


if __name__ == '__main__':
    main()