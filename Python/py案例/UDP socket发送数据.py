# 发送消息
import socket


def send():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7789))  # 绑定端口
    while True:
        send_data = input("请输入发送内容：")

        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.106", 7788))

        if send_data == "exit":
            break
    udp_socket.close()


if __name__ == '__main__':
    send()

