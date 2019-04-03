f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')
"""
This creates a list of strings for each line in the file.
Each item in list will also have the new including newline characters
"""
lines = f.readlines()
"""
This prints out as we would expect, respecting the new line character
"""
#lines = f.read() 
f.close()
print(lines)
