import socket

from config.dev import TEST_HOST_IP
from config.dev import TEST_HOST_SSH_PORT

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((TEST_HOST_IP, TEST_HOST_SSH_PORT))

# receive some data
response = client.recv(4096)
print response
