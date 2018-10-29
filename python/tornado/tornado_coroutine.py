import random
import time
from tornado import gen
from tornado.ioloop import IOLoop

urls = ['URL1', 'URL2', 'URL3']

async def get_url(url):
    wait_time = random.randint(1, 4)
    await gen.sleep(wait_time)
    print('URL {} took {}s to get!'.format(url, wait_time))
    return (url, wait_time)


async def outer_coroutine():
    before = time.time()
    coroutines = [await get_url(url) for url in ['URL1', 'URL2', 'URL3']]
    after = time.time()
    print(coroutines)
    print('total time: {} seconds'.format(after - before))


if __name__ == '__main__':
    IOLoop.current().run_sync(outer_coroutine)