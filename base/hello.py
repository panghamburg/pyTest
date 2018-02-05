import keyword

print(keyword.kwlist)

#字符串
str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + 'TEST')
print('Ru\noob')
print(r'Ru\noob')

#列表
list = ['abcd', 789, 2.3, 'runoob', 70.22]
tinylist = [123, 'run']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(tinylist + list)

#元组
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

#集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if('Rose' in student):
    print('yes')
else:
    print('no')

a = set('abrachadabra')
b = set('alacazam')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#字典
dict = {}
dict['one'] = '1 - 菜鸟教程'
dict[2] = '2 - 菜鸟工具'
tinydict = {'name': 'runoob', 'code':1, 'site': 'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

frozenset()
a = 20
b = 200
if (a is b):
    print(1)
else:
    print(2)
