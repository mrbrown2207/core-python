f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
# Adds a new line to each item in the list
text = '\n'.join(lines)
f.writelines(text)
f.close()
