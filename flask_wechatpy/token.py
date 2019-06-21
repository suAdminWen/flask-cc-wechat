import json
import requests
import datetime
from functools import lru_cache

from flask import current_app


@lru_cache(None)
def _access_token():
    """
    获取微信access token，本地缓存两个小时
    装饰器vald_token会拦截第二个参数，所以该方法在调用时，只需要接收参数access_token
    :return access_token: 微信调用接口凭证
    """
    access_token = ''
    postUrl = 'https://api.weixin.qq.com/cgi-bin/token' + \
              '?grant_type=client_credential&appid={}&secret={}' \
              .format(current_app.config.get('WXAPPID'),
                      current_app.config.get('WXAPPSECRET'))
    url_resp = requests.get(postUrl)
    if url_resp.status_code == 200:
        url_resp = json.loads(url_resp.text)
        access_token = url_resp["access_token"]
    return access_token, datetime.datetime.now()


class TokenUtil:

    def access_token(self):

        token, create_datetime = _access_token()
        if create_datetime < datetime.datetime.now() - \
           datetime.timedelta(hours=2):
            _access_token().cache_clear()
            token, create_datetime = _access_token()
        return token
