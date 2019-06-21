from flask import current_app


class WXConfig(object):
    """ 获取微信配置 """

    def __init__(self):
        self.app_id = current_app.config.get('WXAPPID')
        self.app_secret = current_app.config.get('WXAPPSECRET')
