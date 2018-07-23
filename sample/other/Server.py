from __future__ import print_function
import socket
import select

def main():
	host = '127.0.0.1'
	port = 4000
	backlog = 10
	bufsize = 4096

	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	readfds = set([server_sock])
	try:
		server_sock.bind((host, port))
		server_sock.listen(backlog)

		while True:
			rready, wready, xready = select.select(readfds, [], [])
		
			for sock in rready:
				if sock is server_sock:
					conn, address = server_sock.accept()
					readfds.add(conn)
				else:
					msg = sock.recv(bufsize)
					if len(msg) == 0:
						sock.close()
						readfds.remove(sock)
					else:
						print(msg)
						sock.send(msg)
	finally:
		for sock in readfds:
			sock.close()
	return

if __name__ == '__main__':
	main()
