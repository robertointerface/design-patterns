import queue


def producer(q, count):
    for n in range(count):
        print('producing', n)
        q.put(n)
    print('producer done')
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('consuming', item)
    print('consumer done')
