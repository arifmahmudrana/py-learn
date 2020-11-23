import re

pattern = re.compile(r'(^[a-zA-Z$%#@]{7,}[0-9]$)')
string = 'asdasa$%#@5'

a = pattern.search(string)
print(a)
