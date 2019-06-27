import hashlib
from .exceptions import InvalidSignatureException


def check_signature(token, signature, timestamp, nonce):

    data = sorted([token, timestamp, nonce])
    string = ''.join(data).encode('utf-8')
    hashcode = hashlib.sha1(string).hexdigest()

    if hashcode != signature:
        raise InvalidSignatureException()
