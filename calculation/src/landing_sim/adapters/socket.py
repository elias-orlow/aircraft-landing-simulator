import socket



def create_server_socket():
    host = 'localhost'  # Server ip
    port = 11111        # Server port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print("INFO: Server Started")
        while True:
            conn, addr = s.accept()
            with conn:
                print("INFO: Connected by:", addr)
                data = conn.recv(1024)
                if not data:
                    continue
                text = data.decode('utf-8')
                print("INFO: From connected user: " + text)