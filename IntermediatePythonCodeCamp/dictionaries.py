mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# value = mydict("name")
# print(value)
#
# value = mydict("age")
# print(value)
#
# value = mydict("city")
# print(value)

mydict["email"] = "myemail@email.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")


for key in mydict:
    print(key)

for key, value in mydict.items():
    print(key, value)

mydict_copy = mydict
print(mydict_copy)

mydict_copy = mydict.copy()
print(mydict_copy)

mydict_copy = dict(mydict)
print(mydict_copy)

mydict.update(mydict2)
print(mydict)

mydict.popitem()
print(mydict)


my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

mytuple = (8, 7)
my_dict2 = {mytuple: 15}

print(my_dict2)

