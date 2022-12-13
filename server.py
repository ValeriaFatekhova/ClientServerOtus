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
                res = self.read_client_data(client)
                print(self.create_http_responce(res))

                client.send(self.create_http_responce(res).encode())
                client.close()

    def read_client_data(self, client):
        end_of_stream = '\r\n\r\n'
        str_data = ""
        while True:
            data = client.recv(1024)
            if not data:
                break
            str_data += data.decode("utf-8")
            if end_of_stream in str_data:
                break
        l = str_data.replace("\r", "").split("\n")
        return l

    def create_http_responce(self, client_data):
        http_response = (
            f"HTTP/1.0 200 OK\r\n"
            f"Server: otushomework\r\n"
            f"Date: Sat, 01 Oct 2022 09:39:37 GMT\r\n"
            f"Content-Type: text/html; charset=UTF-8\r\n"
            f"\r\n"
        )
        return http_response


server = TCPServer()
server.server_run("127.0.0.1", 8885)
