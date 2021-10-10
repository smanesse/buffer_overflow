#!/usr/bin/python3
s = input("Address: ")
s = s.replace("0x", "")
for i in range(len(s), 0, -2):
    print("\\x" + s[i-2:i], end="")
print(f"\nDon't forget to set a breakpoint on your address (0x{s}) . Then run ./7jmp_test.py")
