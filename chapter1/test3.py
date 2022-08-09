import re

p = re.compile(r'\w+[w]\w+')

text = 'wonderful'

text2 = 'owner'

a = p.findall(text)

b = p.findall(text2)

print(a, b)