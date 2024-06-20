class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"__new__ called for {name}!")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"__init__ called for {name}!")
        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print(f"__call__ called for {cls} inside MyMeta!")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    @classmethod
    def __new__(cls, *args, **kwargs):
        print(f"__new__ called for {cls}")
        return super().__new__(*args, **kwargs)

    def __init__(self):
        print("__init__ called!")


class MyClass2(metaclass=MyMeta):
    pass


my_obj = MyClass()
