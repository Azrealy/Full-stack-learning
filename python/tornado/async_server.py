class CallBackFailed(Exception):
    pass

def callback_a(callback):
    print("callback_a")
    try:
        callback()
    except Exception:
        raise CallBackFailed("Catch a exception from a")

def callback_b(callback):
    print("callback_b")
    try:
        callback()
    except Exception:
        raise CallBackFailed("Catch a exception from b")

def callback_c():
    print("callback_c")
    raise 'error'

try:
    callback_a(callback_b(callback_c))
except Exception as m:
    print(m)