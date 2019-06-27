
REPLY_TYPES = {}


def register_reply(msg_type):
    def register(cls):
        REPLY_TYPES[msg_type] = cls
        return cls
    return register


@register_reply('empty')
class EmptyReply:
    """
    回复空串

    微信服务器不会对此作任何处理，并且不会发起重试
    """

    def __init__(self):
        pass

    def render(self):
        return ''


@register_reply('text')
class Reply:

    def __init__(self, content, data):
        self.ToUserName = data['FromUserName']
        self.FromUserName = data['ToUserName']
        self.CreateTime = data['CreateTime']
        self.Content = content

    def render(self):
        sendXml = """<xml>
         <ToUserName><![CDATA[%s]]></ToUserName>
         <FromUserName><![CDATA[%s]]></FromUserName>
         <CreateTime>%s</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[%s]]></Content>
         </xml>
        """
        return sendXml % (
            self.ToUserName,
            self.FromUserName,
            self.CreateTime,
            self.Content)


def create_reply(reply, message=None):
    if not reply:
        r = EmptyReply()
    else:
        r = Reply(reply, message)
    return r
