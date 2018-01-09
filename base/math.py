import math
import random
import fibo

math.ceil(11)
ma = random.choice(range(10))
print(ma)

fibo.fib(10)
print(fibo.fib2(10))
mathName = dir(math)
for name in mathName:
    print(name)

s = 'hello, runoob'
print(str(s))
print(repr(s))
print(str(1/7))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(6))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

fil = open('../../test.txt', 'r+')
print(fil.readline())
print(fil.tell())
fil.close()
