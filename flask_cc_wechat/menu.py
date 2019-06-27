import logging
import requests
from . import WECHAT_API_URL
from .token import TokenUtil

logger = logging.getLogger(__name__)


class Menu(object):
    """
    自定义菜单栏
    """

    def __init__(self):
        self.token = TokenUtil.access_token()

    def create(self, postData):
        postUrl = WECHAT_API_URL + \
            "cgi-bin/menu/create?access_token=%s" % self.token
        request = requests.post(postUrl, data=postData.encode('utf-8'))
        if request.status_code == 200:
            return True
        else:
            return False

    def query(self, accessToken):
        postUrl = WECHAT_API_URL + \
            "cgi-bin/menu/get?access_token=%s" % accessToken
        requests.get(postUrl)

    def delete(self, accessToken):
        postUrl = WECHAT_API_URL + \
            "cgi-bin/menu/delete?access_token=%s" % accessToken
        requests.get(postUrl)

    def get_current_selfmenu_info(self, accessToken):
        postUrl = WECHAT_API_URL + \
            "cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        request = requests.get(postUrl)
        return request.text
