#Design a distributed application using RPC for remote computation where client submits an
#integer value to the server and server calculates factorial and returns the result to the client program.

# Server
from xmlrpc.server import SimpleXMLRPCServer
import threading

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def start_server():
    server = SimpleXMLRPCServer(("127.0.0.1", 8000), allow_none=True)
    server.register_function(factorial, "factorial")
    print("Server started on 127.0.0.1:8000")
    server.serve_forever()

threading.Thread(target=start_server, daemon=True).start()

# Client 
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/", allow_none=True)
num=int(input('Enter a number : '))
result = proxy.factorial(num)

print("Factorial:", result)
