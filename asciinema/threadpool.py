from queue import Queue
from threading import Thread
# import time
import urllib.request as ur


def singleton(cls):
    """单例模型"""
    _instance = {}

    def inner(*args):
        if cls not in _instance:
            _instance[cls] = cls(*args)
        return _instance[cls]
    return inner


def send(url: str, upload_data: str)-> None:
    """send data by http post"""
    # with open('2.txt', 'a') as f:
    #     f.write(upload_data + '\n' + url + '\n')
    retries = 3
    while retries:
        try:
            # construct request
            data = upload_data.encode('utf8')
            headers = {'Content-Type': 'application/json'}
            req = ur.Request(url, data, headers)
            req.get_method = lambda: 'PUT'
            # put
            resp = ur.urlopen(req)  # send request
            break
        except Exception as e:
            pass
        finally:
            retries -= 1


class MyThread(Thread):
    def __init__(self, tasks: Queue, endtag):
        Thread.__init__(self)
        self.tasks = tasks
        self.endtag = endtag

    def run(self):
        # print(id(self.tasks))
        # print('start ', self.name)
        for url, upload_data in iter(self.tasks.get, self.endtag):
            send(url, upload_data)
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



