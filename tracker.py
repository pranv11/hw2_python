def func_counter(f):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return f(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y+2**3-34

foo(6)
foo(5)
foo(6)
foo(5)
foo(6)
foo(5)
print(foo.counter)
