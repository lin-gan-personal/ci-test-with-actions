# System Modules
import math
import random

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def generate_two_random_reals(min_val=0.0, max_val=1.0):
    """
    Generates and returns two random real (floating-point) numbers
    within the range [min_val, max_val].
    """
    first_num = random.uniform(min_val, max_val)
    second_num = random.uniform(min_val, max_val)
    return first_num, second_num