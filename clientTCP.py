import socket

target_host = "www.google.com"
target_port = 80

# socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

# send data:
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#client.send(b"GET / HTTP/1.1\r\nhttps://www.google.com/search?q=google+search+post+request\r\n\r\n ")

# recieve data:
response = client.recv(4096)

print(response.decode())
client.close()
