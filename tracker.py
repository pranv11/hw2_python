# def func_counter(fnc):
    
#     def wrapper(*args, **kwargs):
        
#         counter += 1
#         print(counter)
#         return fnc(*args, **kwargs)
#     return wrapper

# @func_counter
# def foo(y):
#     return y+2**3-34

# foo(1)
# foo(1)

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

succ(5)
