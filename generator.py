import base64
import datetime
import time
import json
import hmac
from hashlib import sha1

from exceptions import TooShortTimeout


class OssPolicyAuth():

    def __init__(self,
                 access_key_id,
                 access_key_secret,
                 timeout=60,
                 max_size=10):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret

        # Going to expire in duration seconds
        self.timeout = timeout * 60

    def get_iso_8601(expire):
        gmt = datetime.datetime.utcfromtimestamp(expire).isoformat()
        return "{}Z".format(gmt)

    def get_policy(self):
        timeout = int(time.time()) + self.timeout
        policy_text = {
            "expiration": self.get_iso_8601(timeout),
            "conditions": [
                ['content-length-range', 0, self.maxSize * 1024 * 1024]
            ]
        }
        policy = json.dumps(policy_text)
        return base64.b64encode(policy.encode())

    def get_sign(self):
        policy = self.get_policy()
        h = hmac.new(self.access_key_secret.encode(), policy, sha1)
        return base64.encodestring(h.digest())

    def get_token(self):
        timeout = self.timeout - 5 * 60
        if (timeout <= 0):
            raise TooShortTimeout()

        expire_at = self.get_iso_8601(timeout)

        return {
            "policy": self.get_policy(),
            "signature": self.get_sign(),
            "expire_at": expire_at
        }
