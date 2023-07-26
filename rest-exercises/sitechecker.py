import sys
import socket

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more than two are allowed: \n- http server\'s address (required)\n- port number (defualts to 80 if not specified)")
    exit(1)

fqdn = ""
port = "80"
# print(sys.argv, type(sys.argv))
if len(sys.argv) == 2:
    fqdn = sys.argv[1]
if len(sys.argv) == 3:
    fqdn = sys.argv[1]
    port = sys.argv[2]
    print(type(port), port)

# print(fqdn, port)
if not port.isdigit() or int(port) not in range(1, 65_536):
    print("Port number is invalid - exiting")
    exit(2)

try:
    print('connection')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((fqdn, int(port)))
    
except socket.timeout as te:
    print("Timeout error occured.")
    exit(3)
except Exception as e:
    print(f'{e}')
    exit(4)
else:
    print("Connecting")
    sock.send(b'HEAD / HTTP/1.1\r\nHost: '+ bytes(fqdn, "utf-8") + \
        b'\r\nConnection: close\r\n\r\n'
        ) 
    reply = sock.recv(50)
    # print(reply, type(reply)
    idx = reply.index(b'\r\n')
    print(reply[:idx].decode())    