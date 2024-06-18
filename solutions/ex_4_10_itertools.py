import itertools
import operator

# Generate all possible combinations of rolling two six-sided dice.
dices = list(range(1, 7)) * 2
for roll in itertools.combinations(dices, 2):
    print(roll, end=" ")
print()


# Solve the same problem as exercise 9.2 above, but with starmap.
tuples = [(4, 5), (13, 6), (75, 2), (54, 11), (84, 3)]


def product_of_tuples(tuple_list):
    return list(itertools.starmap(operator.mul, tuple_list))


print(f"Products of tuples' elements: input={tuples}, "
      f"output={product_of_tuples(tuples)}")
