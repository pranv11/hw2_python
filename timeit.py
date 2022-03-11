import time as time

def calculate_time(func):
    def wrapper():
        time_initial =time.time()
        func()
        time_final = time.time()
        print("Total time " + str(time_final-time_initial))
        
        
    return wrapper

@calculate_time
def printe():
    print("hey")


printe()