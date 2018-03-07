import time
import uuid
import redis
import unittest
from .base import JsonStorage

class TestRjs(unittest.TestCase):

    def test01(self):
        conn = redis.Redis()
        storage = JsonStorage(conn)
        data1 = {
            "a": 1,
            "b": 2,
        }
        key = str(uuid.uuid4())
        storage.update(key, data1)
        data2 = storage.get(key)
        assert data1["a"] == data2["a"]

        data3 = {
            "b": 3,
            "c": 4,
        }
        storage.update(key, data3)
        data4 = storage.get(key)
        assert data4["b"] == 3
        assert data4["c"] == 4

        storage.delete_field(key, "b")
        data5 = storage.get(key)
        assert not "b" in data5

        storage.delete(key)

    def test02(self):
        conn = redis.Redis()
        storage = JsonStorage(conn)
        data1 = {
            "a": 1,
            "b": 2,
        }
        key = str(uuid.uuid4())
        storage.update(key, data1)
        storage.delete(key)
        data2 = storage.get(key)
        assert not data2

    def test03(self):
        key = str(uuid.uuid4())
        conn = redis.Redis()
        storage = JsonStorage(conn)
        storage.update(key, None)
        assert not conn.keys(key)

    def test04(self):
        key = str(uuid.uuid4())
        conn = redis.Redis()
        storage = JsonStorage(conn)
        task = {
            "method": "debug.ping",
        }
        storage.update(key, task, 1)
        assert conn.keys(key)
        time.sleep(3)
        print(conn.keys(key))
        assert not conn.keys(key)

