import socket


class UDPServer:
    def server_run(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((host, port))  # host = 127.0.0.1, port = 8888
            res = s.recv(1024)
            print("Message: ", res.decode("utf-8"))
            s.close()


class TCPServer:
    def server_run(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(5)
            while True:
                client, addr = s.accept()
                res = client.recv(1024)
                send_data = {}
                print(res.decode("utf-8"))
                client.send(res)
                client.close()
