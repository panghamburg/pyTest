import calendar
import cmath
import random
import datetime

#
print(calendar.month(2018, 2))
#
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)

print(sol1)
#
print(random.randint(0, 11))
#
num = 11
if(num % 2) == 0:
    print('{0}是偶数'.format(num))
else:
    print('{0}是奇数'.format(num))
#
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(n)
        return True
    except (TypeError, ValueError):
        return False

print(is_number(11))
print(is_number('a'))
#
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
    print(factorial)

#
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'. format(j, i, i * j), end='')
    print()

f1, f2 = 0, 1
num = 5
for i in range(1, num + 1):
    print(f2, end=' ')
    f1, f2 = f2, f1 + f2

#
str = 'runoob.com'
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())
#
print(calendar.monthrange(2018, 2))
#
today = datetime.date.today()
print(today)
day = datetime.timedelta(days=1)
print(day)
print(today - day)

#
li = ["a", "b", "mpilgrim", "z", "example"]
print(li[1:-1])
li.append('new1')
li.insert(1, 'c')
li.extend(['ow', 'oc'])
print(li)
print(li.index('oc'))
li1 = [1, 2, 3]
print([e * 2 for e in li1])
#
