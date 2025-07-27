# Niveau 1

# 1. Liste vide
liste_vide = []

# 2. Liste avec plus de 5 articles
courses = ['pain', 'lait', 'œufs', 'tomates', 'riz', 'jus']

# 3. Longueur de la liste
print("Longueur de la liste:", len(courses))

# 4. Premier, élément moyen et dernier élément
print("Premier:", courses[0])
print("Moyen:", courses[len(courses) // 2])
print("Dernier:", courses[-1])

# 5. Liste mixte
mixtes_data_types = ['Achraf', 25, 1.75, 'Célibataire', 'Lomé']

# 6. Liste IT_COMPANIES
IT_COMPANIES = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Affichage
print("IT_COMPANIES:", IT_COMPANIES)

# 8. Nombre d'entreprises
print("Nombre d'entreprises:", len(IT_COMPANIES))

# 9. Premier, moyen et dernier
print("Premier:", IT_COMPANIES[0])
print("Moyen:", IT_COMPANIES[len(IT_COMPANIES) // 2])
print("Dernier:", IT_COMPANIES[-1])

# 10. Modifier une entreprise
IT_COMPANIES[1] = 'Meta'
print("Après modification:", IT_COMPANIES)

# 11. Ajouter une entreprise
IT_COMPANIES.append('Tesla')
print("Après ajout:", IT_COMPANIES)

# 12. Insérer au milieu
IT_COMPANIES.insert(len(IT_COMPANIES) // 2, 'Netflix')
print("Après insertion milieu:", IT_COMPANIES)

# 13. Remplacer sauf IBM
for i in range(len(IT_COMPANIES)):
    if IT_COMPANIES[i] != 'IBM':
        IT_COMPANIES[i] = 'Up It'
        break
print("Remplacement:", IT_COMPANIES)

# 14. Vérification
print("Google existe-t-elle ?", 'Google' in IT_COMPANIES)

# 15. Trier
IT_COMPANIES.sort()
print("Triée:", IT_COMPANIES)

# 16. Inverser
IT_COMPANIES.reverse()
print("Inversée:", IT_COMPANIES)

# 17. Enlever 3 premières
del IT_COMPANIES[:3]
print("Sans les 3 premières:", IT_COMPANIES)

# 18. Enlever 3 dernières
del IT_COMPANIES[-3:]
print("Sans les 3 dernières:", IT_COMPANIES)

# 19. Société(s) intermédiaire(s)
milieu = len(IT_COMPANIES) // 2
print("Milieu:", IT_COMPANIES[milieu:milieu+1])

# 20. Supprimer la dernière
IT_COMPANIES.pop()
print("Après suppression dernière:", IT_COMPANIES)

# 21. Fusion front-end et back-end
front_end = ['html', 'css', 'js', 'react', 'redux']
back_end = ['node', 'express', 'mongodb']
full_stack = front_end + back_end

# 22. Insertion après Redux
full_stack.insert(full_stack.index('redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print("Full Stack:", full_stack)

# Niveau 2

# 1. Liste d'âges
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Âges triés:", ages)

# Min et max
min_age = min(ages)
max_age = max(ages)
print("Min:", min_age, "Max:", max_age)

# Ajouter min et max à la liste
ages.extend([min_age, max_age])
print("Après ajout:", ages)

# Médiane
ages.sort()
n = len(ages)
median = (ages[n // 2] + ages[n // 2 - 1]) / 2 if n % 2 == 0 else ages[n // 2]
print("Médiane:", median)

# Moyenne
moyenne = sum(ages) / len(ages)
print("Moyenne:", moyenne)

# Écart
print("Écart (abs):", abs(min_age - moyenne))

# 2. Milieu de la liste de pays
pays = ['Chine', 'Russie', 'États-Unis', 'Finlande', 'Suède', 'Norvège', 'Danemark']
milieu_pays = len(pays) // 2
print("Pays du milieu:", pays[milieu_pays])

# 3. Diviser la liste de pays
premiere_moitie = pays[:milieu_pays+1]
deuxieme_moitie = pays[milieu_pays+1:]
print("1ère moitié:", premiere_moitie)
print("2ème moitié:", deuxieme_moitie)

# 4. Déborder les 3 premiers
premiers = pays[:3]
scandiques = pays[3:]
print("Premiers pays:", premiers)
print("Pays scandiques:", scandiques)
