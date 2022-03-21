import time
import socket
import os
import sys
s = socket.socket()
host = input('Enter the host: ')
port = int(input('Enter the port: '))
s.connect((host, port))
print('Connected to the server')
command = s.recv(1024)
comman = command.decode('utf-8')
while True:
    command = input('Enter the command: ')
    s.send(command.encode('utf-8'))
    if command == 'exit':
        s.close()
        sys.exit()
    result = s.recv(1024)
    print(result.decode('utf-8'))
    time.sleep(1)
    command = s.recv(1024)
    comman = command.decode('utf-8')
    if comman == 'exit':
        s.close()
        sys.exit()
    result = s.recv(1024)
s.close()
sys.exit()