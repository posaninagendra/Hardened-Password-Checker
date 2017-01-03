from Crypto.Util.number import long_to_bytes
from Crypto.Hash import HMAC


def prf(key1, key2, msg):
    mac1 = HMAC.new(long_to_bytes(key1))
    mac1.update(msg)
    mac2 = HMAC.new(key2)
    mac2.update(mac1.hexdigest())
    return int(mac2.hexdigest(), 16)