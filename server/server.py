import SocketServer
import os


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        while 1:
            data = self.request.recv(1024).strip()
            if not data:
                break
            # just send back the same data, but upper-cased
            print("received %s" % data)
            self.request.sendall(data.upper())

if __name__ == "__main__":
    HOST, PORT = os.getenv('HOST',''), 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()