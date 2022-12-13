import socket
from http import HTTPStatus


class UDPServer:
    def server_run(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((host, port))
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
        header = ""
        request_method = ""
        request_source = ""
        status_value = 200
        status_phrase = "OK"
        try:
            query_params = client_data[0].split()[1][2:].split("&")
            request_method = client_data[0].split()[0]
            for param in query_params:
                if param[0:6] == "status":
                    status_value = int(param.split("=")[1])
                    status_phrase = HTTPStatus(status_value).phrase
        except:
            status_value = 200
            status_phrase = "OK"

        for param in client_data[1:]:
            if param[0:4] == "Host":
                request_source = param.split()[1]
        header += f"Request Method: {request_method}\r\n"
        header += f"Request Source: {request_source}\r\n"
        header += f"Response Status: {status_value}\r\n"
        for param in client_data[1:]:
            header += f"{param}\r\n"

        http_response = (
            f"HTTP/1.0 {status_value} {status_phrase}\r\n"
            f"{str(header)}\r\n"
            f"\r\n"
        )
        return http_response


server = TCPServer()
server.server_run("127.0.0.1", 8885)
