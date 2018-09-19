### Example 9-9: A directory listing socket client

## Usage: run ch09_08.py in one command-line window and ch09_09 in another,
## then in the second, at the @ prompt type a filename pattern, e.g. *.py,
## and get bck a list of all the matching files in the directory in which
## ch09_08.py is running.

import socket

HOST = socket.gethostname()
PORT = 5500                                                # The server's listener port number
encoding = 'ASCII'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # standard
s.connect((HOST, PORT))
sockname = s.getsockname()
print('Connected to', sockname[0], 'on port', sockname[1])

try:
    data = input('@ ')
    while data:
        s.send(data.encode(encoding))
        data = s.recv(1024).decode(encoding)
        print(data)
        data = input('@ ')
except (EOFError, KeyboardInterrupt):
    pass
finally:
    s.close()
