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
        key = "876712da-737a-43a1-990d-61fb6cd12ac5"
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

    def test02(self):
        conn = redis.Redis()
        storage = JsonStorage(conn)
        data1 = {
            "a": 1,
            "b": 2,
        }
        key = "876712da-737a-43a1-990d-61fb6cd12ac6"
        storage.update(key, data1)
        storage.delete(key)
        data2 = storage.get(key)
        assert not data2


