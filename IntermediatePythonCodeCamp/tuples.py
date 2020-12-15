import sys
import timeit

myTuple = ("Max", 28, "Boston")
print(type(myTuple))

myTuple = tuple(["Max", 28, "Boston"])
print(myTuple)

item = myTuple[0]
print(item)

for i in myTuple:
    print(i)


if "Max" in myTuple:
    print("yes")
else:
    print("no")

myTuple2 = ('a', 'p', 'p', 'l', 'e')
print(len(myTuple2))

print(myTuple2.count('p'))

print(myTuple2.index('p'))

my_list = list(myTuple2)
print(my_list)
myTuple3 = tuple(my_list)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)

my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple2
print(i1)
print(i3)
print(i2)


my_list = [0, 1, 2, "hello", True]
my_tuple3 = (0,1, 2, "hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple3), "bytes")


print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
