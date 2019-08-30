import socket


def main():
    # 创建TCP套接字，socket.AF_INET使用ipv4
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    # server_ip = input('要连接的IP：')
    # server_port = int(input('要连接的port：'))
    # server_addr = (server_ip, server_port)

    server_addr = ('127.0.0.1', 8888)

    tcp_socket.connect(server_addr)

    while True:
        # 发送数据/接受数据
        send_data = input('发送数据：')
        tcp_socket.send(send_data.encode())

        # 接收数据
        recdata = tcp_socket.recv(1024)
        print('接收到的数据：', recdata.decode())

        if send_data == 'exit':
            break

    #关闭套接字
    tcp_socket.close()




if __name__ == '__main__':
    main()
