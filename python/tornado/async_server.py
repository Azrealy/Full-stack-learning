def coroutine():
    while True:
        receive = yield
        print("Receive: ", receive)

coro = coroutine()
next(coro)
coro.send("hello")
coro.send("world")