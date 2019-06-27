import xmltodict

from messages import MESSAGE_TYPES, UnknownMessage
from events import EVENT_TYPES


def parse_message(xml):
    """
    解析微信服务器推送的 XML 消息
    :param xml: XML 消息
    :return: 解析成功返回对应的消息或事件，否则返回 ``UnknownMessage``
    """
    if not xml:
        return
    message = xmltodict.parse(xml)['xml']
    message_type = message['MsgType'].lower()
    event_type = None
    if message_type == 'event':
        if 'Event' in message:
            event_type = message['Event'].lower()

        message_class = EVENT_TYPES.get(event_type, UnknownMessage)
    else:
        message_class = MESSAGE_TYPES.get(message_type, UnknownMessage)
    return message_class(message)
