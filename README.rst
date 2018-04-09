redis-json-storage
==================

.. image:: https://travis-ci.org/appstore-zencore/redis-json-storage.svg?branch=master
    :target: https://travis-ci.org/appstore-zencore/redis-json-storage

Reids json storage. Store json data as hashmap in redis.

Install
-------

::

    pip install redis-json-storage

Class & Methods
-----

1. redis_json_storage.JsonStorage

   a. update
   b. get
   c. delete
   d. delete_field


Example
-----

::

    from redis_json_storage import JsonStorage

    connection = make_redis_connect(config)
    storage = JsonStorage(connection)
    data1 = {
        "a": 1,
        "b": 2,
    }
    storage.update(data1)
    data2 = {
        "b": 3,
        "c": 4,
    }
    storage.update(data2)
    data3 = storage.get(key)
