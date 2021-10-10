HOST = ""
PORT = 0
PREFIX = b""
TOTAL_LENGTH = 0
OFFSET = 0
EIP = b"BBBB"


def initial(s):
    s.recv(1024)
    s.send(b"")
    # etc
