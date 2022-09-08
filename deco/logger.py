# Logging keeps track of how many times a specif function is run 
# Keeps track of what arguments where past to that function


# from time import time


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and Kwargs: {kwargs}")
        return orig_func(*args, **kwargs)
    return wrapper

# Timer for any program
def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in sec {t2}")
        return result
    
    return wrapper
import time

@my_logger
@my_timer
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Tresure', 23)

