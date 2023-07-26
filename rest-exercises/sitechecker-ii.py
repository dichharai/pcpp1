import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more than two are allowed: \n- http server\'s address (required)\n- port number (defualts to 80 if not specified)")
    exit(1)

fqdn = ""
port = "80"

if len(sys.argv) == 2:
    fqdn = sys.argv[1]
elif len(sys.argv) == 3:
    fqdn = sys.argv[1]
    port = sys.argv[2]

# print(fqdn, port)
if not port.isdigit() or int(port) not in range(1, 65_536):
    print("Port number is invalid - exiting")
    exit(2)

try:
    reply = requests.head("http://localhost:3000/")
    print(reply)
except requests.Timeout:
    print("Timeout")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(f'Content-Type: {reply.headers["Content-Type"]}')
        print(f'reply: {reply.content.decode()}, dir: {dir(reply)}')
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("server error")

