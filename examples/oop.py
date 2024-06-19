from datetime import date


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self.increment_count()

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

    def get_age(self):
        return self.years_passed_since(self.date_of_birth)

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def years_passed_since(date_obj):
        today = date.today()
        age = today.year - date_obj.year
        if (date_obj.month, date_obj.day) > (today.month, today.day):
            age -= 1
        return age


class Student(Person):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


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

    print(p1.get_age())
    print(Person.get_age(p1))

    print(p1.count is Person.count)

    # p1.increment_count()
    # Person.increment_count()
    print("Person count:", Person.count)

    print(Person.years_passed_since(date(1918, 12, 1)))
