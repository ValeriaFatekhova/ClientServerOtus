from server import TCPServer, UDPServer

server = TCPServer()
server.server_run("127.0.0.1", 8888)
