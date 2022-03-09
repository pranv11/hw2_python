def doubler(fnc):
    def wrapper():
        fnc()
        fnc()
    return wrapper
