from queue import Queue
from threading import Thread
import time


def singleton(cls):
    _instance = {}

    def inner(*args):
        if cls not in _instance:
            _instance[cls] = cls(*args)
        return _instance[cls]
    return inner


class MyThread(Thread):
    def __init__(self, tasks: Queue, endtag):
        Thread.__init__(self)
        self.tasks = tasks
        self.endtag = endtag

    def run(self):
        # print(id(self.tasks))
        # print('start ', self.name)
        for task_data in iter(self.tasks.get, self.endtag):
            # time.sleep(10)
            with open('2.txt', 'a') as f:
                f.write(task_data + '\n')
        # print('end ', self.name)


@singleton
class Tpool:
    def __init__(self, thread_num=1):
        self.tasks = Queue()
        self.thread_num = thread_num
        self.threads = []
        self.endtag = None
        self.sequence_num = 0  # 序列号
        for i in range(self.thread_num):
            t = MyThread(self.tasks, self.endtag)
            t.start()
            self.threads.append(t)

    def put(self, task):
        self.tasks.put(task)

    def end(self):
        for i in range(self.thread_num + 1):
            self.tasks.put(self.endtag)
        for t in self.threads:
            t.join()



