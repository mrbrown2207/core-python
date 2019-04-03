import re

import collections

"""
f = open("data.txt", "r+")
lines = f.readlines()
print(lines)
lines[0] = "New line 1\n"
lines[2] = "New line 3\n"
f.seek(0)
f.write(''.join(lines))
f.flush()
f.seek(0)
lines = f.read()
print(lines)

f.close()
"""

f = open("data.txt", "r+")
lines = f.readlines()
print(lines)
f.seek(0)
f.write("foo 1")
f.seek(len(lines[0]) + len(lines[1]))
f.write("foo 3")
f.flush()
f.seek(0)
lines = f.read()
print(lines)
f.close()



