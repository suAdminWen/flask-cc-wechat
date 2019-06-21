import json
import requests
from urllib.parse import urlencode

from flask import current_app


class Authorized(object):
    """
    用户同意授权
    """

    def __init__(self):
        self.app_id = current_app.config.get('WXAPPID')
        self.app_secret = current_app.config.get('WXAPPSECRET')

    def getCode(self, redirect_url, state):
        """
        获取code, 并跳转到指定界面
        """
        # 转换之后的url中将 :  // 等字符进行了转换
        params = urlencode({"redirect_uri": redirect_url})
        request_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}".format(self.app_id) + \
                      "&{}".format(params) + \
                      "&response_type=code&scope=snsapi_userinfo&" + \
                      "state={}".format(state) + "#wechat_redirect"
        return request_url

    def getAcToken(self, code):
        """
        通过code换取网页授权access_token
        """
        request_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=" + self.app_id + \
                      "&secret=" + self.app_secret + \
                      "&code=" + code + \
                      "&grant_type=authorization_code"
        response = requests.get(request_url)
        if response.status_code == 200:
            the_page = response.text
            jsonreturn = json.loads(the_page)
            if 'errcode' not in jsonreturn:
                return jsonreturn["access_token"], jsonreturn["openid"]
        return None, None

    def getUserInfo(self, access_token, openId):
        request_url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN"\
            .format(access_token, openId)
        response = requests.get(request_url)
        if response.status_code == 200:
            the_page = response.text
            jsonreturn = json.loads(the_page)
            if 'errcode' not in jsonreturn:
                return jsonreturn
        return {}
