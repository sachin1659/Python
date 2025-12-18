"""
========================================================
PYTHON DECORATORS — FULL EXPLANATION WITH CODE EXAMPLES
========================================================

A decorator is a function (or class) that:
- Takes another function as input
- Adds extra behavior
- Returns a new function

Decorators do NOT modify the original function’s code.
They wrap it.
"""

# -----------------------------------------------------
# 1. FUNCTIONS ARE FIRST-CLASS OBJECTS
# -----------------------------------------------------

def say_hello():
    return "Hello!"

# Functions can be assigned to variables
greet = say_hello
print(greet())  # Hello!


# -----------------------------------------------------
# 2. FUNCTIONS CAN BE NESTED
# -----------------------------------------------------

def outer():
    def inner():
        return "Inner function"
    return inner

fn = outer()
print(fn())  # Inner function


# -----------------------------------------------------
# 3. BASIC DECORATOR (NO ARGUMENTS)
# -----------------------------------------------------

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        result = func()
        print("After the function runs")
        return result
    return wrapper


@my_decorator
def say_hi():
    print("Hi!")

# Equivalent to:
# say_hi = my_decorator(say_hi)

say_hi()


# -----------------------------------------------------
# 4. DECORATOR WITH FUNCTION ARGUMENTS
# -----------------------------------------------------

def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments received:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@decorator_with_args
def add(a, b):
    return a + b

print(add(3, 5))


# -----------------------------------------------------
# 5. DECORATOR WITH RETURN VALUE
# -----------------------------------------------------

def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


@double_result
def multiply(a, b):
    return a * b

print(multiply(3, 4))  # (3 * 4) * 2 = 24


# -----------------------------------------------------
# 6. PRESERVING FUNCTION METADATA (functools.wraps)
# -----------------------------------------------------

from functools import wraps

def proper_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper


@proper_decorator
def example():
    """Original function docstring"""
    pass

print(example.__name__)  # example
print(example.__doc__)   # Original function docstring


# -----------------------------------------------------
# 7. DECORATOR WITH ITS OWN ARGUMENTS
# -----------------------------------------------------

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# -----------------------------------------------------
# 8. CLASS-BASED DECORATOR
# -----------------------------------------------------

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count}")
        return self.func(*args, **kwargs)


@CountCalls
def say_bye():
    print("Bye!")

say_bye()
say_bye()


# -----------------------------------------------------
# 9. REAL-WORLD EXAMPLE: TIMING A FUNCTION
# -----------------------------------------------------

import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)

slow_function()


# -----------------------------------------------------
# 10. STACKING DECORATORS
# -----------------------------------------------------

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper


@bold
@italic
def text():
    return "Hello"

print(text())  # <b><i>Hello</i></b>


"""
========================================================
SUMMARY
========================================================
- Decorators wrap functions
- Use @decorator syntax
- Use *args, **kwargs for flexibility
- Use functools.wraps to preserve metadata
- Can be functions or classes
- Used for logging, auth, timing, caching, validation
"""
