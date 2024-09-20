import socket
import threading

"""
Write a socket-server chat-server that accepts clients that connect to it over TCP. 
An example client would be telnet.

Creating MVP version with the most basic functionality.
Connect and disconnect with multiple client support and basic message forwarding:

The chat server should be capable of handling multiple clients connecting at the same time.
Disconnection should be handled in a clean way.
Should be able to receive and forward messages among clients (message is not echoed back to sender).
"""
clients = []
nicknames = set()

def handle_client(client_socket, client_address, nickname):
	print("enters handle_client")
	while True:
		try:
			print("entered try statement")
			message = client_socket.recv(1024)
			#the client closed the connection and the loop is terminated
			if not message: 
				break
			decoded_message = message.decode('utf-8')
			print(f"Received message from {client_address}:{decoded_message}")
			broadcast(f"{nickname}: {decoded_message}".encode('utf-8'), client_socket)
		except:
			print(f"{nickname} has left the chat!")
			clients.remove(client_socket)
			nicknames.remove(nickname)
			client_socket.close()

	#broadcast to all other clients

def broadcast(message, current_client):
	for client in clients:
		if current_client != client: 
			try:
				client.send(message)
			#if message fails to send
			except:
				clients.remove(client)
				client.close()

def start_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('0.0.0.0', 12345))
	server_socket.listen()

	while True:
		client_socket, client_address = server_socket.accept()

		client_socket.send("Welcome to my chat server! What is your nickname?\n".encode('utf-8'))
		nickname = client_socket.recv(1024).decode('utf-8').strip()
		nicknames.add(nickname)

		clients.append(client_socket)
		print(f"{client_socket} has joined!")
		thread = threading.Thread(target = handle_client, args=(client_socket, client_address, nickname))
		thread.start()


if __name__ == "__main__":
	start_server()
