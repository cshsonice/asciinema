import json
from asciinema.config import ConnectParam
from asciinema.threadpool import Tpool


def upload2server(dataline: str):

    cp = ConnectParam()
    upload_data = {
        'data': dataline,               # operation data
        'id':   cp.connect_uuid,        # current ssh uuid
        'ip':   cp.connect_ip,          # current ssh user's ip
        'dt':   cp.connect_datetime,    # establish time of ssh connection
    }
    upload_data = json.dumps(upload_data)
    url = cp.upload_url
    tpool = Tpool()
    tpool.put((url, upload_data))





