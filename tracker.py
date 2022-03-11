def func_counter(f):
    def wrapped(*args, **kwargs):
        wrapped.counter += 1
        return f(*args, **kwargs)
    wrapped.counter = 0
    return wrapped
