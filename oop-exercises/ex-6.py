from datetime import datetime

def log_timestamp(func):
    def log_ts(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        print(f"Evaluated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return log_ts

@log_timestamp
def my_add(a, b):
    return a+b

@log_timestamp
def my_sub(a, b):
    return a - b


my_add(1, 2)
my_sub(1, 2)