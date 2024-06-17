import datetime

# 1. Choose a class - be it a built-in type like int, str, dict, or from a
# Standard Library module like datetime.date or even from a 3rd party library,
# like requests.Request. Instantiate the class. You now have two names: the
# class and the object. Call print, str, repr, type and dir on both these names.
print("Inspecting date type")
print(datetime.date)
print(str(datetime.date))
print(repr(datetime.date))
print(type(datetime.date))
print(dir(datetime.date))

my_date = datetime.date(2021, 10, 12)
print("Inspecting a date object")
print(my_date)
print(str(my_date))
print(repr(my_date))
print(type(my_date))
print(dir(my_date))


# 2. Call help on the following:
# a module
# a function
# a class
# a method of a class
# a method of an object
# You can use the class and object in exercise 1, or new ones.
help(datetime)
help(print)
help(datetime.date)
help(datetime.date.weekday)
help(my_date.weekday)
