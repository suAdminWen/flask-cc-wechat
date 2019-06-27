from flask_cc_wechat.messages import BaseMessage

EVENT_TYPES = {}


def register_event(event_type):
    """
    Register the event class so that they can be accessed from EVENT_TYPES

    :param event_type: Event type
    """
    def register(cls):
        EVENT_TYPES[event_type] = cls
        return cls
    return register


class BaseEvent(BaseMessage):
    """Base class for all events"""
    type = 'event'
    event = ''


@register_event
class SubscribeEvent(BaseEvent):
    type = 'subscribe'
    key = 'EventKey'


@register_event
class ViewEvent(BaseEvent):
    type = 'view'


@register_event
class ClickEvent(BaseEvent):
    type = 'click'
    key = 'not_open'  # 获取messages中的EventKey的值
