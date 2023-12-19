PI = (3.1415,)
# PI = (3, 1415)
print(type(PI))
print(PI)

PI = 5.987
print(PI)

radijus = 5

opseg = 2 * radijus * PI
print(opseg)
print(PI)

# employees = ('Pero PEric', 'Marko Maric', 'Iva Ivic', 'Ana Anic')
employees = 'Pero PEric', 'Marko Maric', 'Iva Ivic', 'Ana Anic'
# print(employees)
print('ID', id(employees))

for employee in employees:
    print(employee)

print('id', id(employees[ : 2]))

print(type(employees))
