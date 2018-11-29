import importlib

MSG_LIST = [
    "my_log.my_message.send_app.SendApp"
]


# 创建一个通用的发送消息的函数
def send_msgs(my_dict):
    # print(f"tan1{my_dict}")
    ret = {
        "level": my_dict.get("level"),
        "project": my_dict.get("project"),
        "principal": my_dict.get("principal"),
        "ip": my_dict.get("ip"),
        "info": my_dict.get("detail"),
        "time": my_dict.get("time"),
    }
    # print(ret)
    for path in MSG_LIST:
        m, c = path.rsplit('.', maxsplit=1)
        md = importlib.import_module(m)
        my_obj = getattr(md, c)()
        msg = my_obj.send(ret)
        return msg
