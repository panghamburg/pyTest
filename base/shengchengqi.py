from enum import Enum
import logging
L = [x * x for x in range(10)]
g = (x * x for x in range(3))

print(g)
print(next(g))
print(next(g))
print(next(g))
for n in g:
    print(n)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum()
print(lazy_sum(1, 3, 5, 7, 9))

def f(x):
    return x * x

f = lambda x: x * x
print(f(6))

e = lambda n: n % 2 == 1
print(e(3))

def now():
    print(1)

f = now
print(f.__name__)

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def set_score(self, score):
        self.__score = score

bart = Student('Bart simpson', 59)
bart.set_score(99)
print(bart.print_score())

class Cl(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender

#继承多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
print(dog.run())

cat = Cat()
print(cat.run())

print(isinstance(dog, Dog))
print(type(123))
print(type('tre'))
print(len('abc'))
print('abc'.__len__())
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(obj.y)

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

stu = Student
print(Student('a').count)
print(Student('b').count)

#限制方法
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('interger!')
        if value < 0 or value > 100:
            raise ValueError('between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
#装饰器

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('interger!')
        if value < 0 or value > 100:
            raise ValueError('between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 70
print(s.score)

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f)
print(f[0:5])
print(f[:10])
print(f[:10:2])
#枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(type(Month))

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('Finally...')
print('END')

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

s = '0'
n = int(s)
# logging.info('n = %d' % n)
print(10 / n)
