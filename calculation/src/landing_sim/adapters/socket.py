import socket


# ----- This method creates a socket (IPv4 / TCP) -----
# This socket acts as the host listening on port: '11111', whilst the C# socket acts as the client.
# WIP: right now data send from the client is printed on the console
def create_server_socket():
    host = 'localhost'  # Server ip
    port = 11111        # Server port

    # --- Create socket object ---
    # socket.socket(family, type) -> creates a socket object
    # socket.AF_INET -> IPv4 Socket
    # socket.SOCK_STREAM -> TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # --- Configure socket options ---
        # socket.setsockopt(level, option, value) -> set socket options
        # socket.SOL_SOCKET -> general socket level options
        # socket.SO_REUSEADDR -> allows to bind to the same address even if the connection is still being cleaned up
        # 1 -> boolean value for true
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))
        s.listen() # socket is ready to accept incoming connections
        print("INFO: Server Started") # Log message
        while True:
            # when a client tries to connect, the socket accepts the connection
            # conn -> socket that represents the actual connection channel between the python server and c# client
            # addr -> tuple containing the IPv4 address and port
            conn, addr = s.accept()
            with conn:
                print("INFO: Connected by:", addr) # Log message
                data = conn.recv(1024) # receive up to 1024 bytes of data
                if not data: # client has closed the sending connection
                    continue
                text = data.decode('utf-8') # decode the bytes to utf-8 text
                print("INFO: From connected user: " + text) # Log message