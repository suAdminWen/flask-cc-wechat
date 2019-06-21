import json
import datetime
from functools import lru_cache, wraps

import requests

from .base import WXConfig


def vald_token(func):
    """
    获取有效的token
    对token进行拦截，超过两个小时的token会重新获取
    该装饰器func返回参数有两个，但是第二个参数create_datetime会被拦截掉，
    所以func方法只会对外返回一个在有效期的参数token
    """
    @wraps(func)
    def in_valid_token(*args, **kwargs):
        token, create_datetime = func(*args, **kwargs)
        lnvalid_time = datetime.datetime.now() - datetime.timedelta(hours=2)
        if create_datetime < lnvalid_time:
            func.cache_clear()
            token, create_datetime = func(*args, **kwargs)
        return token
    return in_valid_token


@vald_token
@lru_cache(None)
def get_access_token():
    """
    获取微信access token，本地缓存两个小时
    装饰器vald_token会拦截第二个参数，所以该方法在调用时，只需要接收参数access_token
    :return access_token: 微信调用接口凭证
    """
    access_token = ''
    wx = WXConfig()
    postUrl = 'https://api.weixin.qq.com/cgi-bin/token' + \
              '?grant_type=client_credential&appid={}&secret={}' \
              .format(wx.app_id, wx.app_secret)
    url_resp = requests.get(postUrl)
    if url_resp.status_code == 200:
        url_resp = json.loads(url_resp.text)
        access_token = url_resp["access_token"]
    return access_token, datetime.datetime.now()


@vald_token
@lru_cache(None)
def get_jsapi_ticket():
    """
    获取jsapi ticket，本地缓存两个小时
    :return access_token: 微信调用接口凭证
    """
    jsapi_ticket = ''
    access_token = get_access_token()
    postUrl = "https://api.weixin.qq.com/cgi-bin/ticket" \
        "/getticket?access_token=%s&type=jsapi" % access_token
    url_resp = requests.get(postUrl)
    if url_resp.status_code == 200:
        url_resp = json.loads(url_resp.text)
        jsapi_ticket = url_resp["ticket"]
    return jsapi_ticket, datetime.datetime.now()
