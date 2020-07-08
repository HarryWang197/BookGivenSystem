#!/usr/bin/env python3
# @Time    : 2020/4/24 11:06
# @Author  : Harry Wang
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_async_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    msg = Message('[网上赠书系统]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    # current_app app = Flask()
    app = current_app._get_current_object()
    # 异步发送电子邮件，理由：快
    thread = Thread(target=send_async_mail, args=[app, msg])
    thread.start()
