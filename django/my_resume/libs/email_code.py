# !/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random,string


def random_num():
    # _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
    # _upper_cases = _letter_cases.upper()  # 大写字母
    _numbers = ''.join(map(str, range(0, 10)))  # 数字
    init_chars = ''.join((string.ascii_letters, _numbers))
    my_code = random.sample(init_chars, 6)
    my_code = "".join(my_code)
    return my_code


def email_send(email, email_code):
    my_sender = '342321394@qq.com'  # 发件人邮箱账号
    my_pass = 'ukdvfbhezqzzcaji'  # 发件人邮箱密码
    receive_user = email  # 收件人邮箱账号，我这边发送给自己

    ret = True
    try:
        msg = MIMEText(email_code, 'plain', 'utf-8')
        msg['From'] = formataddr(["简历登录", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", receive_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "简历验证码"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [receive_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
