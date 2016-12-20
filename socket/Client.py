from socket import *

#Address and Port
HOST = '127.0.0.1'
PORT = 21234
ADDR = (HOST, PORT)

#BufferSize
BUFSIZ = 1024

#build socket
tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
	data = raw_input('> ')
	if not data:
		break;

	#send data
	tcpCliSocket.send(data)
	#recv data
	data = tcpCliSocket.recv(BUFSIZ)

	if not data:
		break;

	print data

tcpCliSocket.close()