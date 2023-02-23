import socket

target_host = "127.0.0.1"
target_port = 9998

def main():
    # socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect client
    client.connect((target_host, target_port))

    # send data:
    client.send(b"Hello from the other side.\r\n\r\n")
    # client.send(b"GET / HTTP/1.1\r\nhttps://www.google.com/search?q=google+search+post+request\r\n\r\n ")

    # receive data:
    response = client.recv(4096)

    print(response.decode())
    client.close()


if __name__ == "__main__":
    main()