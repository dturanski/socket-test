import socket
import time
import os
import sys

HOST, PORT = os.getenv('HOST',os.getenv('HOSTNAME','localhost')), 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    data = sys.argv[1] if len(sys.argv) >= 2  else 'hello'
    # Connect to server and send data
    print ("connecting to %s:%d" %(HOST, PORT))
    sock.connect((HOST, PORT))
    while 1:
        sock.sendall(data + '\n')
        time.sleep(1)

    # Receive data from the server and shut down
        received = sock.recv(1024)
        print "Received: {}".format(received)

finally:
    sock.close()


