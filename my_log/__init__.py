import datetime,logging
import socket
from functools import wraps
from my_log import save_send

# def getLevelName(level):
#     result = _levelToName.get(level)
#     if result is not None:
#         return result
#     result = _nameToLevel.get(level)
#     if result is not None:
#         return result
#     return "Level %s" % level
_level = {
    "info": 1,
    "waring": 2,
    "error": 3,
}
waring = 2


class Logger(object):
    def __init__(self):
        # self.sysstr = platform.system()  # 系统类型(linux 还是windows)
        self.name = None
        self.project = None
        self.ip = socket.gethostbyname(socket.gethostname())  # 系统IP
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间
        self.my_dict = {}
        self.level = 1 # 设置告警等级
        self.msg=""

    # 设置告警人
    def set(self, name, project, config):
        self.name = name  # 告警人姓名
        self.project = project
        self.config = config
        return "信息设置成功"

    def timenow(func):
        @wraps(func)
        def inner(self, msg,level):
            self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return func(self, msg,level)
        return inner

    #信息输入
    @timenow
    def data_handle(self,msg,level):
        self.level = level
        self.msg = msg
        self.my_dict = {
            "project": self.project,
            "level": self.level,
            "detail": self.msg,
            "principal": self.name,
            "ip": self.ip,
            "time": self.time
        }
        return save_send.send_if(self.config, self.my_dict)



# 实例化root
root = Logger()


def set(name=None, project=None,config=None):
    return root.set(name, project,config)


# 判断参数设置
def setvalue(func):
    @wraps(func)
    def inner(msg):
        try:
            if root.name and root.project and root.config:
                pass
            else:
                raise ValueError("请先设置好项目和告警人和存储的数据库")
        except ValueError as e:
            print(e)
            return None
        return func(msg)
    return inner


# 正常
@setvalue
def info(msg,level=_level.get("info")):
    return root.data_handle(msg, level)


# 预告警
@setvalue
def waring(msg,level=_level.get("waring")):
    return root.data_handle(msg,level)




@setvalue
def error(msg,level=_level.get("error")):
    return root.data_handle(msg, level)

