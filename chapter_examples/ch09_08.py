### Example 9-8: A directory listing socket server

import socket
import glob

HOST = socket.gethostname()         # Instead of '', allows access over LAN
PORT = 5500                         # Arbitrary nonprivileged port

# listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # standard
s.bind((HOST, PORT))
lisname = s.getsockname()
print('Listening on host', lisname[0], 'port', lisname[1])
s.listen(1)

# create actual socket
conn, addr = s.accept()
sockname = conn.getsockname()
print('Connection from', addr[0], 'on port', addr[1])

try:
    data = conn.recv(1024)
    while data:
        print(data)
        conn.sendall(b'\n'.join(glob.glob(data)))
        data = conn.recv(1024)
except KeyboardInterrupt:
    pass
finally:
    try:
        conn.close()
        s.close()
    except:
        pass
