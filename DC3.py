#Write code to simulate requests coming from clients and distribute them among the servers
#using the load balancing algorithms.

def round_robin(requests):
    servers = ['Server 1','Server 2','Server 3']
    n = len(servers)
    
    for i in range(len(requests)):
        server = servers[i%n]
        print(f'Request {requests[i]} -> {server}')
        
def least_connections(requests):
    servers = {
        'Server 1':0,
        'Server 2':0,
        'Server 3':0
    }
    for req in requests:
        server = min(servers,key=servers.get)
        print(f'Request {req} -> {server}')
        servers[server]+=1
        
requests = [1,2,3,4,5,6,7]
print('Choose your load balancing algorithm :')
print('1. Round Robin')
print('2. Least Connection Load Balancing')
ch=int(input('Enter your choice (1/2) :'))
if ch == 1 :
    print('\nRound Robin Allocation :')
    round_robin(requests)
elif ch == 2 :
    print('\nLeast Connections Allocation :')
    least_connections(requests)
else:
    print('Invalid Choice')
