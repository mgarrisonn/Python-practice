# itertools: product, permulations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat


a = [1, 2]
b = [3]
prod = product(a, b)
prod2 = product(a, b, repeat=2)
print(list(prod))
print(list(prod2))


a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm2 = permutations(a, 2)
print(list(perm2))


a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

a = [1, 2, 3, 4]
acc = accumulate(a)
acc = accumulate(a, func=operator.mul)
acc = accumulate(a, func=operator.max)
print(a)
print(list(acc))


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
groupby_obj = groupby(a, key=smaller_than_3)
for key, value in groupby_obj:
    print(key, list(value))


groupby_obj = groupby(a, key=lambda x: x < 3)
for key, value in groupby_obj:
    print(key, list(value))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

groupby_obj = groupby(persons, key=lambda x: x ['age'])
for key, value in groupby_obj:
    print(key, list(value))


for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)

for i in repeat(1, 4):
    print(i)


