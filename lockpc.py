import socket

# Set up a socket to listen for commands
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.20.10.2', 5555))  # Replace with your desired port
server_socket.listen(1)

def unlock_desktop():
    # Code to unlock the desktop
    pass

while True:
    client_socket, _ = server_socket.accept()
    command = client_socket.recv(1024).decode()
    
    if command == "unlock":
        # Authenticate if necessary
        unlock_desktop()
        client_socket.send("Desktop unlocked".encode())
    else:
        client_socket.send("Invalid command".encode())

    client_socket.close()
