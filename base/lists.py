import os
print(list(range(1, 11)))
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

lists = []
for d in os.listdir('D:/'):
    lists.append(d)
print(lists)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 18, 'Apple', None]
L2 = []
x = 'abd'
a = isinstance(x, str)
print(a)
for s in L:
    if(isinstance(s, str)):
        n = L.index(s)
        L.pop(n)
        L.insert(n, s.lower())
print(L)
