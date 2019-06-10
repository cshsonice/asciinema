import json
from asciinema.config import ConnectParam
from asciinema.threadpool import Tpool


def upload2server(dataline: str):

    cp = ConnectParam()
    postdata = {
        'data': dataline,               # operation data
        'id':   cp.connect_uuid,        # current ssh uuid
        'ip':   cp.connect_ip,          # current ssh user's ip
        'dt':   cp.connect_datetime,    # establish time of ssh connection
    }
    postdata = json.dumps(postdata)
    url = cp.upload_url
    tpool = Tpool()
    tpool.put((url, postdata))





