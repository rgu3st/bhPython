import socket

target_host = "127.0.0.1"
target_port = 54242

# Socket Objs
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data:
client.sendto(b"Helloo!!", (target_host, target_port))

# Receive data:
data, addr = client.recvfrom(4096)

print(data.decode())
client.close
