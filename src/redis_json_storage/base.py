import json


class JsonStorage(object):
    """Store json data in redis as hashmap type.
    """
    def __init__(self, connection, prefix=""):
        self.connection = connection
        self.prefix = prefix

    def make_key(self, key):
        key = self.prefix + key
        return key

    def update(self, key, data=None, expire=None):
        if data:
            mapping = {}
            for k, v in data.items():
                mapping[k] = json.dumps(v)
            key = self.make_key(key)
            self.connection.hmset(key, mapping)
        if expire:
            self.connection.expire(key, expire)

    def get(self, key):
        key = self.make_key(key)
        mapping = self.connection.hgetall(key)
        data = {}
        for k, v in mapping.items():
            if not isinstance(k, str):
                k = k.decode("utf-8")
            if not isinstance(v, str):
                v = v.decode("utf-8")
            data[k] = json.loads(v)
        return data

    def delete(self, key):
        key = self.make_key(key)
        self.connection.delete(key)

    def delete_field(self, key, field):
        key = self.make_key(key)
        self.connection.hdel(key, field)
