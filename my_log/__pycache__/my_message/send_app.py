from my_log.my_message.base import Base
import requests


# APP发送
class SendApp(Base):
    def send(self, my_dict):
        msg = {
            "code": 0,
            "msg": "发送成功"
        }
        url = "http://cyfta.cyou-inc.com/engine/engine/send.action"
        my_get = requests.post(url, data=my_dict)
        my_success = my_get.json()
        if my_success.get("success") != True:
            msg["code"] = 1
            msg["msg"] = my_success.get("msg")
        return msg
