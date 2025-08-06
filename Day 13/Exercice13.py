# Jour 13 - Exercices Python

# 1. Filtrer uniquement négatifs et zéro
nombres = [-4, -3, -2, -1, 0, 2, 4, 6]
negatifs_et_zero = [n for n in nombres if n <= 0]
print("1. Négatifs et zéro :", negatifs_et_zero)

# 2. Aplatir une liste de listes de listes
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplatir = [n for sublist in list_of_lists for inner in sublist for n in inner]
print("2. Liste aplatie :", aplatir)

# 3. Liste de tuples (i, 1, i, i^2, ..., i^6)
table = [(i, 1, i, i**2, i**3, i**4, i**5, i**6) for i in range(11)]
print("3. Table des puissances :")
for ligne in table:
    print(ligne)

# 4. Aplatir la liste de pays avec abréviation
pays = [[('Finlande', 'Helsinki')], [('Suède', 'Stockholm')], [('Norvège', 'Oslo')]]
aplatir_pays = [[p[0], p[0][:3], p[1]] for row in pays for p in row]
print("4. Pays avec abréviation :", aplatir_pays)

# 5. Transformer la liste de pays en dictionnaires
dicts = [{'country': p[0], 'city': p[1]} for row in pays for p in row]
print("5. Liste de dictionnaires :", dicts)

# 6. Liste de noms concaténés
noms = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat = [' '.join(p) for pair in noms for p in pair]
print("6. Noms concaténés :", concat)

# 7. Fonction lambda pour pente et intercept Y
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

# Exemple :
print("7. Exemple de pente et interception :")
print("Pente :", slope(1, 2, 3, 6))
print("Intercept Y :", intercept(1, 2, 3, 6))
