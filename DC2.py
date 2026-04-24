#Design a distributed application using RMI for remote computation where client submits two
#strings to the server and server returns the concatenation of the given strings.

import Pyro4
import threading
import time

@Pyro4.expose
class StringService:
    def concatenate(self, s1, s2):
        return s1 + s2

uri_container={}

def start_server():
    daemon = Pyro4.Daemon()
    uri= daemon.register(StringService)
    uri_container['uri']=uri
    print("Server started...")
    daemon.requestLoop()

# Start server in background thread
threading.Thread(target=start_server, daemon=True).start()

# Wait 2 seconds so server starts properly
time.sleep(2)

# CLIENT PART
proxy = Pyro4.Proxy(uri_container['uri'])
a=input('Enter first string : ')
b=input('Enter second string : ')
result = proxy.concatenate(a,b)

print("Concatenated Result:", result)
