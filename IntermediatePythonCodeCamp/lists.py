# Lists ordered, mutable, allow duplicate elements
myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = [5, True, "apple", "apple"]
print(myList2)

item = myList[0]
print(item)

for i in myList:
    print(i)

if "banana" in myList:
    print("yes")
else:
    print("no")

print(len(myList))

myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

item = myList.pop()
print(item)
print(myList)

item = myList.remove("cherry")
print(myList)

item = myList.clear()
print(myList)

item = myList.reverse()
print(myList)


myList3 = [4, 3, 1, -1, -5, 10]
print(myList3)

item = myList3.sort()
print(myList3)

new_list = sorted(myList)
print(myList3)
print(new_list)

myList4 = [0] * 5
print(myList4)

myList5 = [1, 2, 3, 4, 5]

new_list = myList4 + myList5
print(new_list)

myList6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = myList6[1:5]
print(a)

b = myList6[::2]
print(b)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
# list_cpy = list(list_org)
# list_cpy = list_org[:]
list_cpy.append("lemon")
print(list_cpy)
print(list_org)


c = [1, 2, 3, 4, 5, 6]
d = [i*i for i in c]

print(c)
print(d)


