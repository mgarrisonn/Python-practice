# Strings: ordered, immutable, text representation
from timeit import default_timer as timer

my_string = "Hello World"
my_string1 = 'Hello World'
my_string2 = "I'm a programmer"
my_string3 = 'I\'m a programmer'
my_string4 = """Hello 
World"""
my_string5 = """Hello \
World"""


print(my_string)
print(my_string1)
print(my_string2)
print(my_string3)
print(my_string4)
print(my_string5)


char = my_string[0]
print(char)

substring = my_string[:5]
print(substring)

substring2 = my_string[::1]
print(substring2)

substring3 = my_string[::-1]
print(substring3)

substring4 = my_string[::2]
print(substring4)


greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print('yes')
else:
    print('no')


my_string6 = '    Hello World     '
my_string6 = my_string6.strip()
print(my_string6)


print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('Hello'))
print(my_string.endswith('World'))
print(my_string.find('o'))
print(my_string.count('p'))
print(my_string.replace('World', 'Universe'))


my_string7 = 'how are you doing'
my_list = my_string7.split()
print(my_list)

my_string8 = 'how,are,you,doing'
my_list2 = my_string8.split(",")
print(my_list2)

new_string = ' '.join(my_list)
print(new_string)

my_list3 = ['a'] * 6
print(my_list3)

# bad
start = timer()
my_string11 = ''
for i in my_list3:
    my_string11 += i
stop = timer()
print(my_string11)
print(stop-start)

# good
start = timer()
my_string = ''.join(my_list3)
stop = timer()
print(my_string)
print(stop-start)


# %, .format, f-Strings
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.1234567
my_string = "the variable is %f" % var
print(my_string)

var = 3.1234567
my_string = "the variable is %.2f" % var
print(my_string)

var = 3.1234567
my_string = "the variable is {}".format(var)
print(my_string)

var = 3.1234567
my_string = "the variable is {:.2f}".format(var)
print(my_string)

var = 3.1234567
var2 = 7
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

var = 3.1234567
var2 = 7
my_string = f"the variable is {var} and {var2}"
print(my_string)

var = 3.1234567
var2 = 7
my_string = f"the variable is {var*2} and {var2}"
print(my_string)
