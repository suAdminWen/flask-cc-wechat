class Wechat(object):

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(self.app)

    def init_app(self, app):

        self.app_id = self.app.config.get('WXAPPID')
        self.app_secret = self.app.config.get('WXAPPSECRET')

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        print('wechat')
