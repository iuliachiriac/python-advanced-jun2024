from datetime import date


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __int__(self):
        return self.date_of_birth.year

    def __str__(self):
        return f"{type(self).__name__} object (name={self.name}, "\
               f"dob={self.date_of_birth})"

    def __repr__(self):
        return f"{type(self)} object at {id(self)}"

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __le__(self, other):
        return self.date_of_birth >= other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Anna", date(1989, 5, 9))
    p2 = Person("John", date(1996, 12, 8))
    p3 = Person("Mike", date(1996, 12, 8))

    print(Person.__name__, Person.__bases__, Person.__module__)
    print(p1.__dict__)

    print(int(p1))

    print(str(p1), repr(p1))

    print(p1 < p2)  # p1.__lt__(p2)
    print(p2 <= p3)  # p1.__le__(p2)
    print(p1 > p2)
    print(p2 == p3)
