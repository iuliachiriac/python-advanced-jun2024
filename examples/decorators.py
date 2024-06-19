from functools import wraps


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"I am {func.__name__} and I got decorated")
        print(f"Decorated function arguments: args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print()
        return result

    return inner


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@make_pretty
@repeat(3)
def ordinary():
    print("I am ordinary")


# ordinary = repeat(3)(ordinary)  # decorator_repeat(ordinary)

@make_pretty
def greet(name):
    """Prints a greeting message for name"""
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=0):
    return nr - step


if __name__ == "__main__":
    # ordinary = make_pretty(ordinary)
    ordinary()  # make_pretty.<locals>.inner()

    # print(ordinary)

    greet("John")  # make_pretty.<locals>.inner("John")
    greet(name="Anna")  # make_pretty.<locals>.inner(name="Anna")

    decrement_result = decrement(10, 2)
    print("Decrement result:", decrement_result)

    print("greet attributes:", greet.__name__, greet.__doc__)
    help(greet)
