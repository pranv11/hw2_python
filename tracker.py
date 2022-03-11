def func_counter(func):
    
    def something(counter = 0):
        
        func()
        counter += 1
    
    return something  


