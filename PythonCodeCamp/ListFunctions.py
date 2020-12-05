lucky_numbers = [7, 11, 34, 10, 9]
friends = ["Kevin", "Jason", "Trey", "Jason", "Alan", "Joe"]
print(friends)

friends.append("John")
print(friends)

friends.insert(1, "Jane")
print(friends)

friends.remove("Trey")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

print(friends.count("Jason"))

friends.sort()
print(friends)

friends2 = friends.copy()
print(friends2)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.clear()
print(friends)

