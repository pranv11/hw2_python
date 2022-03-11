def function(func):
    def something(*arg):
        something.aNumber += 1
        function(*arg)
    something.counter = 0
    return something  
