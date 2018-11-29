from my_log import comdb
from my_log import my_message


def send_if(config, my_dict):
    """
    :param config:config = {
    'host': '0.0.0.0',
    'port': 3306,
    'user': 'xxx',
    'passwd': 'xxx',
    'db': 'logs',
    'charset': 'utf8'
}
    :param my_dict: {
            "project": self.project,  #项目
            "level": self.level, #类型
            "detail": self.msg, #详情
            "principal": self.name, #负责人
            "ip": self.ip, # 主机IP
            "time": self.time #时间
    :return:
    """
    ret = {
        "db_code": 0,
        "send_code": 1,
        "msg": "没有发送",
    }
    try:
        comdb.mysql(config=config, my_dict=my_dict)
    except:
        ret["db_code"] = 1
    if my_dict.get("level") > 1:
        data = my_message.send_msgs(my_dict)
        ret["send_code"] = data.get("code")
        ret["msg"] = data.get("msg")
    return ret
