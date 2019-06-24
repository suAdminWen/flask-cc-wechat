from flask import Flask
from flask_wechatpy import Wechat
from flask_wechatpy.token import TokenUtil

app = Flask(__name__)

app.config['WXAPPID'] = 'wx2828f4c1e66df8f6'
app.config['WXAPPSECRET'] = '3df70973737d409d6f9f740585e53d18'

wx = Wechat()
wx.init_app(app)


@app.route('/')
def index():
    tokenb = TokenUtil.access_token()
    print(tokenb)

    return 'ok'


if __name__ == '__main__':
    app.run()
