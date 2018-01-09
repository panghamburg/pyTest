#部分内建函数
import sys
import string
from collections import deque
str = 'the is Test'
list = ['ab', 'cd', 'ef']
a = 11
print(str.capitalize()) #第一个字转大写
print(str.count('t'))
print(str.find('i'))
print(str.index('i'))
print(','.join(list))
print(str.endswith('s'))
print(str.lower())
print(str.upper())

list = ['Google', 'Runoob', 1997, 2000, 1997]
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']

# del list[0]
# print(list[1])
print(list.index(1997))
list.append('hello')
print(list)
print(list.count(1997))
list.extend(list1)
list.remove(1997)
list.reverse()
print(list)

tup = ('Google', 'Runoob', 1997, 2000, 1997)
tup1 = (1, 2, 3, 4, 5)
tup2 = ('a', 'b', 'c', 'd')

print(len(tup))
print(tuple(list1))

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#del dict['Name']
print(dict.copy())
seq = ('name', 'age', 'sex')
print(dict.fromkeys(seq))
print(dict.items())
dict.update({'sex': 's'})
print(dict)
print(dict.popitem())
print(dict.pop('Name'))

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b
# age = int(input('输入一个整数:'))
# if age < 0:
#     print(1)
# elif age == 2:
#     print(3)
# else:
#     print(2)

#猜数字
num = 7
guess = -1
print('猜数字！')
# while guess != num:
#     guess = int(input('输入数字:'))
#     if guess == num:
#         print('OK')
#     elif guess < num:
#         print('litter')
#     elif guess > num:
#         print('big')

languages = ['c', 'c++', 'perl', 'python']
for x in languages:
    print(x)

for i in range(5):
    print(i)

for i in range(0, 10, 3):
    print(i)

#遍历列表
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行pass')
    print('当前字母:', letter)
print('end')

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))

def fibonacci(n):
    a, b ,counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)

# while True:
#     try:
#         print(next(f), end=" ")
#         #结束迭代
#     except StopIteration:
#         sys.exit()
s = lambda arg1, arg2: arg1 + arg2
print(s(10, 29))
num = 1
def fun1():
    global num
    print(num)
    num = 123
    print(num)
fun1()

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)

outer()

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
print(queue)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

#转换列表
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

dict1 = {x: x**2 for x in (2, 4, 6)}
print(dict1)

#遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for k, v in enumerate(knights):
    print(k, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is you {0}? It is {1}.'.format(q, a))

print(sys.path)
