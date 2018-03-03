rjs
===

Reids json storage.

Install
-------

::

    pip install rjs

Class & Methods
-----

1. rjs.JsonStorage

   a. update
   b. get
   c. delete
   d. delete_field


Example
-----

::

    from rjs import JsonStorage

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
