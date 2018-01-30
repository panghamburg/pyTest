import json
import os
from multiprocessing import Process
from multiprocessing import Pool
import time, random
from multiprocessing import Process, Queue

# d = dict(name='Bob', age=20, score=88)
# json.dumps(d)
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score,
#     }
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('我的子进程(%s) 和 父进程是(%s)' % (os.getpid(), os.getppid()))
# else:
#     print('我(%s) 创建一个子进程(%s)' % (os.getpid(), pid))

#window 下进程线程
# def run_proc(name):
#     print('子进程 %s' % os.getpid())
#
# if __name__ == '__main__':
#     print('父进程 %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     p.start()
#     p.join()

#批量新建进程
# def long_time_task(name):
#     print('分派 %s (%s)' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('分派 %s 运行 %0.2f seconds' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print('父类进程 %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有子进程...')
#     p.close()
#     p.join()
#     print('所有子进程运行')

#进程通讯
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('%s 压入队列..' % value )
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('进程读取: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('从队列获取 %s' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
