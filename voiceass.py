import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Reserve a port
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection.
server_socket.listen(1)  # Listen for only one connection

print("Waiting for incoming connection from phone...")

# Accept a connection from the client (phone)
client_socket, client_address = server_socket.accept()

print("Phone connected:", client_address)

# Receive data from the client
data = client_socket.recv(1024).decode()
print("Received data from phone:", data)

# Close the connection with the client
client_socket.close()

# Close the server socket
server_socket.close()
