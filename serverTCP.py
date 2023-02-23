import socket
import threading
import rjg_common

IP = '0.0.0.0'  # Accept from all incoming
PORT = 9998
THREAD_ID = 0
# Just client: IANA and RFC 6335 suggest the range 49152–65535, (2^15+2^14):(2^16 − 1) for dynamic or private ports.


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"- Listening on port {PORT}")

    while True:
        client, address = server.accept()
        print(f"- Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    global THREAD_ID
    print(f"Spun up new client thread {THREAD_ID}")
    THREAD_ID += 1
    with client_socket as sock:
        request = sock.recv(4096)  # The book uses 1024, but I've seen larger chunks be more efficient these days.
        print(f"- Recieved: {request.decode('utf-8')}")
        sock.send(b'ACK')


if __name__ == "__main__":
    main()


