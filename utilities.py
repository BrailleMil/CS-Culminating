import random

def get_valid_int(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt))
            if low is not None and value < low:
                continue
            if high is not None and value > high:
                continue
            return value
        except ValueError:
            continue

def apply_random_discount(total):
    if random.randint(1,5) == 1:
        return total * 0.9
    return total
