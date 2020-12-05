is_male = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")


is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")


is_tall = True
is_male = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")


is_tall = True
is_male = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")


is_tall = False
is_male = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")


is_tall = True
is_male = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are not male or not tall or both")


is_tall = False
is_male = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are not male or not tall or both")


is_tall = True
is_male = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")


is_tall = False
is_male = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")

is_tall = False
is_male = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")
