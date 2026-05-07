#--------------------------------------------------DECORATOR-------------------------------------------------------------#
#-----------------------------------------------TASK 25-06-2025----------------------------------------------------------#


# 1. WAP to create a decorator to calculate program execution time

import time

def execution_timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start, "seconds")
        return result
    return inner

@execution_timer
def sample_task():
    for i in range(1000000):
        pass

sample_task()

#---------------------------------------------------------------------------------------------------------------#
# 2. WAP to create a decorator which should return a positive value always.

def ensure_positive(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return inner

@ensure_positive
def subtract(a, b):
    return a - b

print("Result:", subtract(5, 10))  


# -------------------------------------------------------------------------------------------------------------------- #
# 3. WAP to create a decorator which should give 5s of delay time

import time

def delay_5_sec(func):
    def inner(*args, **kwargs):
        print("Delaying for 5 seconds...")
        time.sleep(5)
        return func(*args, **kwargs)
    return inner

@delay_5_sec
def say_hello():
    print("Hello after 5 seconds!")

say_hello()

# -------------------------------------------------------------------------------------------------------------------- #


#--------------------------------------------------DECORATOR COMBINATION-------------------------------------------------------------#
#-----------------------------------------------TASK 25-06-2025----------------------------------------------------------#

import time

# Decorator to measure execution time
def execution_timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start, "seconds")
        return result
    return inner

# Decorator to add 5 seconds delay
def delay_5_sec(func):
    def inner(*args, **kwargs):
        print("Delaying for 5 seconds...")
        time.sleep(5)
        return func(*args, **kwargs)
    return inner

# Applying both decorators: delay first, then measure time (decorators apply inside-out)
@execution_timer
@delay_5_sec
def sample_task():
    for i in range(1000000):
        pass
    print("Task completed.")

# Calling the decorated function
sample_task()

