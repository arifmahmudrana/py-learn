import time


def performance(delay=0):
    time1 = time.time()
    time.sleep(delay)
    time2 = time.time()
    print(f'paused for {time2-time1} s')

    def decorator(func):
        def wrapper(*args, **kwargs):
            time1 = time.time()
            result = func(*args, **kwargs)
            time2 = time.time()
            print(f'took {time2-time1} s')

            return result

        return wrapper

    return decorator


@performance(delay=2)
def sleep_for(sleep_time):
    time.sleep(sleep_time)


print(sleep_for(2))
