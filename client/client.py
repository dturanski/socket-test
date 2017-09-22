import socket
import time
import os


HOST, PORT = os.getenv('HOST',os.getenv('HOSTNAME','localhost')), 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    print ("connecting to %s:%d" %(HOST, PORT))
    sock.connect((HOST, PORT))
    while 1:
        sock.sendall("hello\n")
        time.sleep(1)

    # Receive data from the server and shut down
        received = sock.recv(1024)
        print "Received: {}".format(received)

finally:
    sock.close()


