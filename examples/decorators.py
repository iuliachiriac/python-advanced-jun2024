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


@make_pretty
def ordinary():
    print("I am ordinary")


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
