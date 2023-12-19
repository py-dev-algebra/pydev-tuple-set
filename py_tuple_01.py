lista = ['Pero Peric', 'Ana Anic', 'Iva Ivic']
rjecnik = {
    'first_name': 'Pero',
    'last_name': 'Peric',
    'year_of_birth': 1998
}

#              0               1          2             3
n_terac = ('Pero Peric', 'Ana Anic', 'Iva Ivic', 'Ana Anic')

for element in n_terac:
    print(element, end='; ')
print()

print(n_terac[1])

# n_terac[1] = 'Marko Maric'
# print(n_terac[1])

print(n_terac.index('Ana Anic'))

print(tuple(lista))