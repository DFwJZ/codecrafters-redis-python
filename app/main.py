# Uncomment this to pass the first stage
import socket
import threading

def handle_connection(client_connection, client_addr):
    while True:
        try:
            client_connection.recv(1024) # limit input to 1024 byte of data
            msg = b"+PONG\r\n"
            client_connection.send(msg)
        except ConnectionError:
            break # handling if connection closed

def redis_connect():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    print("start connecting.....")

    while True:
        client_connection, client_addr = server_socket.accept()
        threading.Thread(target=handle_connection, args=(client_connection,client_addr)).start()


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    redis_connect()
    
if __name__ == "__main__":
    main()
