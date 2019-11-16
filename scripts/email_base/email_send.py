# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/11/16 15:18


from envelopes import Envelope

userEmail = "xxx@xxx.com"

html=f"""
<div>66</div>
"""

def send_msg():
    envelope = Envelope(  # 实例化Envelope
        from_addr=(userEmail),  # 必选参数，发件人信息。前面是发送邮箱，后面是发送人；只有发送邮箱也可以
        to_addr=(userEmail),  # 必选参数，发送多人可以直接(u'user1@example.com'， u'user2@example.com')
        subject=f"",  # 必选参数，邮件标题
        # html_body=html,  # 可选参数，带HTML的邮件正文
        text_body=u"I'm a helicopter!",  # 可选参数，文本格式的邮件正文
        cc_addr=[userEmail],  # 可选参数，抄送人，也可以是列表形式
        bcc_addr=[userEmail],  # 可选参数，隐藏抄送人，也可以是列表
        headers=u'',  # 可选参数，邮件头部内容，字典形式
        charset=u'utf-8',  # 可选参数，邮件字符集
    )
    envelope.add_attachment('E:\迅雷下载\11.jpg')  # 增加附件，注意文件是完整路径，也可以加入多个附件

    envelope.send('xxx.xxx.com')  # 发送邮件，分别是smtp服务器，登陆邮箱，登陆密码，tls设置


if __name__ == "__main__":
    send_msg()
