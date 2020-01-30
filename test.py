"""
このファイルに解答コードを書いてください
"""
from os import path
a = path.join(path.dirname(__file__), 'input.txt')
dictionary_i_s = {}

with open(a) as f:
    l_strip = [s.strip() for s in f.readlines()]
    # print(l_strip)

m = int(l_strip[-1])
for index,l in enumerate(l_strip):
    if index==len(l_strip)-1:
        break
    i,s = l.split(':')
    dictionary_i_s[int(i)] = s
dict_sorted = sorted(dictionary_i_s.items(),key=lambda x:x[0])
ans = ''
for elem in dict_sorted:
    if m % elem[0] == 0:
        ans = ans + elem[1]
if ans=='':
    print(m)
else:
    print(ans)