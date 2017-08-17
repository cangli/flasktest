from gevent import monkey
monkey.patch_all()
from gevent import pool
import time


def test():
    print('start')
    time.sleep(5)
    print('end')
p = pool.Pool()

for i in range(10):
    p.apply_async(test)
p.join()
