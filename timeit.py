import time

def calculate_time(fnc):
    def wrapper():
        time_initial = time.time()
        fnc()
        time_final = time()

        print("Total time " + str(time_final-time_initial))
    return wrapper

