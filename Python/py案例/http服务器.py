import socket
import re
# import select

def service_client(new_socket, request):
    request_lines = request.splitlines()
    print('-'*100)

    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0].decode())
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    try:
        f = open('D:/Net' + file_name, 'rb')
    except:
        respose = 'HTTP/1.1 404 NOT FOUNDD\r\n\r\n404'
        new_socket.send(respose.encode())
    else:
        html_content = f.read()
        f.close()

        respose_header = 'HTTP/1.1 200 OK\r\nContent-length:%d\r\n\r\n' % len(html_content)
        respose = respose_header.encode() + html_content
        new_socket.send(respose)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.setblocking(False)
    tcp_server_socket.bind(('', 80))
    tcp_server_socket.listen(128)

    # 创建一个epoll对象
    # epl = select.epoll()

    client_socket_list = []


    while True:
        try:
            new_client_socket, client_addr = tcp_server_socket.accept()
            print(client_addr)
        except Exception as ret:
            pass
        else:

            new_client_socket.setblocking(False)
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
                print(recv_data.decode())
            except Exception as ret:
                pass
            else:
                if recv_data:
                    # 对方发送来的数据
                    # 返回消息
                    service_client(client_socket, recv_data)
                else:
                    client_socket_list.remove(client_socket)
                    client_socket.close()
                    print('对方已关闭')


if __name__ == '__main__':
    main()