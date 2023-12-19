# Kreirati tuple od 100 brojeva od 1 do 100 (uklj.)

brojevi = []

for element in range(1, 101):
    brojevi.append(element)

brojevi_tuple = tuple(brojevi)

print(brojevi_tuple)
