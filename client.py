import socket


class UDPClient:
    def client_run(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(b"UDP Test message", (host, port))


class TCPClient:
    def client_run(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(b"TCP Test message")


client = TCPClient()
client.client_run("127.0.0.1", 8888)
