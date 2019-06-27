import json
import time

import requests

from . import WECHAT_API_URL
from .token import TokenUtil


MESSAGE_TYPES = {}


def register_message(msg_type):
    def register(cls):
        MESSAGE_TYPES[msg_type] = cls
        return cls
    return register


class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
    """

    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __setattr__(self, key, value):
        self[key] = value


class BaseMessage(object):
    type = 'unknown'
    source = ""
    target = ""
    create_time = str(int(time.time()))

    def __init__(self, message):
        self._date = message

    def __repr__(self):
        return '{klass}{msg}'.format(
            klass=self.__class__.__name__,
            msg=repr(self._data))

    def __get__(self, instance, instance_type):
        if instance is not None:
            value = instance._data.get(self.attr_name)
            return value

    def __set__(self, instance, value):
        instance._data[self.attr_name] = value


@register_message('text')
class TextMessage(BaseMessage):
    type = 'text'
    content = '接收'  # 获取message中的Content的值


class UnknownMessage(object):
    pass


class SendMessage(object):
    """
    给用户发送信息
    """

    def __init__(self):
        self.ToUserName = ""
        self.FromUserName = ""
        self.CreateTime = str(int(time.time()))
        self.MsgType = ""
        self.Content = ""

    def send_tm_message(self, postdata):
        access_token = TokenUtil.access_token()
        post_url = WECHAT_API_URL + \
            "cgi-bin/message/template/send?access_token=%s" % access_token

        response = requests.post(post_url, data=postdata.encode('utf-8'))
        jsonreturn = json.loads(response.text)
        print(jsonreturn)
        if jsonreturn["errcode"] == 0:
            return True
        else:
            return False
