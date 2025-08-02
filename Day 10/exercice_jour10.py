# Jour 10 - 30 Days of Python

# NIVEAU 1

# 1. Itérer 0 à 10 avec for
for i in range(11):
    print(i)

# 1. Itérer 0 à 10 avec while
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Itérer 10 à 0 avec for
for i in range(10, -1, -1):
    print(i)

# 2. Itérer 10 à 0 avec while
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Triangle avec #
for i in range(1, 8):
    print("#" * i)

# 4. Boucles imbriquées pour grille de #
for i in range(6):
    for j in range(13):
        print("#", end=' ')
    print()

# 5. Affichage du motif de multiplication
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Itérer dans la liste
techs = ["python", "numpy", "pandas", "django", "flask"]
for tech in techs:
    print(tech)

# 7. Imprimer uniquement les nombres pairs de 0 à 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8. Imprimer uniquement les nombres impairs de 0 à 100
for i in range(101):
    if i % 2 != 0:
        print(i)


# NIVEAU 2

# 1. Somme de tous les nombres de 0 à 100
total = 0
for i in range(101):
    total += i
print("La somme de tous les nombres est:", total)

# 2. Somme des pairs et des impairs
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("La somme de tous les nombres pairs est:", sum_even)
print("La somme de tous les nombres impairs est:", sum_odd)


# NIVEAU 3

# 1. Pays contenant 'land'
from data.Pays import countries

land_countries = []
for country in countries:
    if 'land' in country['name']:
        land_countries.append(country['name'])
print("Pays contenant 'land':", land_countries)

# 2. Inverser une liste de fruits
fruits = ["banane", "orange", "mangue", "citron"]
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Fruits inversés:", reversed_fruits)

# 3. Données sur les pays
from data.Pays_data import countries_data

# i. Nombre total de langues
all_languages = []
for country in countries_data:
    all_languages.extend(country['languages'])

unique_languages = set(all_languages)
print("Nombre total de langues:", len(unique_languages))

# ii. 10 langues les plus parlées
from collections import Counter
language_count = Counter(all_languages)
top_10_languages = language_count.most_common(10)
print("Top 10 des langues les plus parlées:")
for lang, count in top_10_languages:
    print(f"{lang}: {count}")

# iii. 10 pays les plus peuplés
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_10_populated = sorted_by_population[:10]
print("Top 10 des pays les plus peuplés:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']}")
