import json
from asciinema.config import ConnectParam
from asciinema.threadpool import Tpool


def upload2server(dataline: str):

    cp = ConnectParam()
    postdata = {
        'data': dataline,
        'id':   cp.connect_uuid,
        'ip':   cp.connect_ip,
    }
    postdata = json.dumps(postdata)
    send(postdata)


def send(data: str):
    tpool = Tpool()
    tpool.put(data)





