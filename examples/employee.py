class InvalidPercent(Exception):
    pass


class Employee:
    ACCEPTED_RAISE_VALUES = (5, 10, 20)

    def __init__(self, name, bank_account, salary=0):
        self.name = name
        self._bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent):
        if percent not in self.ACCEPTED_RAISE_VALUES:
            raise InvalidPercent(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary