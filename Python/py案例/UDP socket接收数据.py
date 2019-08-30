import socket

# 接收消息
def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 创建套接字
    # 绑定一个本地信息
    localaddr = ('', 7788)
    udp_socket.bind(localaddr)
    while True:
        # 接收信息 储存的是元祖(接收到的数据, (发送方IP，port))
        recv_data = udp_socket.recvfrom(1024)  # 1024表示最大字节

        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 打印
        print('%s:%s' % (str(send_addr), recv_msg.decode('utf-8')))

        if recv_msg.decode('utf-8') == 'exit':
            break
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

