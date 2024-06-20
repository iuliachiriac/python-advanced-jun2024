import pytest

from employee import Employee, InvalidPercent


@pytest.fixture
def employee():
    return Employee("John Doe", None, 1000)


@pytest.fixture
def fix():
    print("Setup code")
    yield None
    print("Teardown code")


def test_valid_percent(employee):
    employee.raise_salary(10)
    assert employee.salary == 1100


def test_invalid_percent(employee):
    with pytest.raises(InvalidPercent):
        employee.raise_salary(25)
