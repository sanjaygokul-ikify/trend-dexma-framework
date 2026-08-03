import time

metrics = {}

def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        metrics[func.__name__] = end_time - start_time
        return result
    return wrapper
