def singleton(cls):
    """单例模型"""
    _instance = {}

    def inner(*args):
        if cls not in _instance:
            _instance[cls] = cls(*args)
        return _instance[cls]
    return inner

