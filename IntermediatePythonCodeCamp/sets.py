# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

myset2 = set([1, 2, 3])
print(myset2)

myset3 = set("Hello")
print(myset3)

myset4 = set()
print(type(myset4))

myset4.add(1)
myset4.add(2)
myset4.add(3)

for i in myset4:
    print(i)


if 1 in myset4:
    print("yes")

myset4.remove(3)
myset4.discard(4)
myset4.pop()
print(myset4)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.difference_update(setB)
print(setA)


setA.symmetric_difference_update(setB)
print(setA)

print(setA.issubset(setB))

print(setB.issuperset(setA))

print(setA.isdisjoint(setB))

setD = setA.copy()
print(setD)

setD = set(setA)
print(setD)


a = frozenset([1, 2, 3, 4])
print(a)
