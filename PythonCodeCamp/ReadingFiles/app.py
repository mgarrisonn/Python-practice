
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines())


employee_file.close()

