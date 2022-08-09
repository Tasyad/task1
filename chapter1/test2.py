# 2. Написать программу с использованием регулярного выражения, которая найдет
# строковое значение, в котором есть буква ‘w’ только не в начале слова и не в конце.
# text1 = "wonderful" # None
# text2 = "owner" # match object
import re
pattern = r".+w.+"
text1 = '''
wonderful
owner
'''
res = re.search(pattern, text1)
if res:
    print('Match!')
    print(res.group())
else:
    print('Not a Match!')