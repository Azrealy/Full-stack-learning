# -*- coding: utf-8 -*-
import time
from tornado import gen
from tornado.ioloop import IOLoop

@gen.coroutine
def get_user_info(id):
    print('----before get user info-----')
    yield gen.sleep(1) # Change here use blocking process like time.sleep()
    print('----after get user info-----')
    user = 'user %s' % str(id)
    return user

@gen.coroutine
def get():
    before = time.time()
    result = yield [get_user_info(i) for i in range(4)]
    after = time.time()
    print(result)
    print('total time: {} seconds'.format(after - before))

if __name__ == '__main__':
    IOLoop.current().run_sync(get)

"""
----before get user info-----
----before get user info-----
----before get user info-----
----before get user info-----
----after get user info-----
----after get user info-----
----after get user info-----
----after get user info-----
['user 0', 'user 1', 'user 2', 'user 3']
total time: 1.0029628276824951 seconds
"""