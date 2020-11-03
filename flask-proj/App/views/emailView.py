from flask import Blueprint
from flask_mail import Message

from App.ext_init import mail

eBlue = Blueprint('eBlue', __name__)


@eBlue.route('/send_email/')
def send_email():
    msg = Message("这是标题",
                  sender="z2234261505@163.com",
                  recipients=["z2234261505@163.com"])
    msg.body = '这是正文'
    mail.send(msg)
    return '发送成功'
