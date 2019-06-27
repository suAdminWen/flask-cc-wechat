class WeChatException(Exception):
    """Base exception for wechatpy"""

    def __init__(self, errcode, errmsg):
        """
        :param errcode: Error code
        :param errmsg: Error message
        """
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return 'Error code: {code}, message: {msg}'.format(
            code=self.errcode,
            msg=self.errmsg
        )

    def __repr__(self):
        return '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errcode,
            msg=self.errmsg
        )


class InvalidSignatureException(WeChatException):
    """Invalid signature exception class"""

    def __init__(self, errcode=-40001, errmsg='Invalid signature'):
        super(InvalidSignatureException, self).__init__(errcode, errmsg)
