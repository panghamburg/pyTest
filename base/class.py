import urllib.request
print(dir(urllib.request))
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n,
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))

class student(people):
    grage = 0
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grage = int(g)
    def speak(self):
        # print(self.grage)
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grage))

s = student('ken', 10, 60, 3)
print(s.speak())

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
