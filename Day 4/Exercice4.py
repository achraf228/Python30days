# Exercices - Jour 4 

# 1. Concaténation
resultat1 = "trente" + " " + "jours" + " " + "de" + " " + "python"
print("1.", resultat1)

# 2. Concaténation
resultat2 = "codage" + " " + "pour" + " " + "tous"
print("\n2.", resultat2)

# 3-5. Variable société
societe = "codage pour tous"
print("\n3-5. Société:", societe, "- Longueur:", len(societe))

# 6-7. Majuscules/minuscules
print("\n6.", societe.upper())
print("7.", societe.lower())

# 8. Formatage
chaine = "Coding For All"
print("\n8. Capitalize:", chaine.capitalize())
print("   Title:", chaine.title())
print("   Swapcase:", chaine.swapcase())

# 9. Premier mot
print("\n9. Premier mot:", chaine.split()[0])

# 10. Vérification sous-chaîne
print("\n10. Contient 'codage':", "codage" in societe)

# 11. Remplacement
print("\n11.", societe.replace("codage", "Python"))

# 12. Correction
print("\n12.", "Python pour tout le monde".replace("tout le monde", "tous"))

# 13. Split
print("\n13.", societe.split())

# 14. Split par virgule
print("\n14.", "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

# 15-17. Indexation
print("\n15. Premier caractère:", chaine[0])
print("16. Dernier index:", len(chaine) - 1)
print("17. Caractère à l'index 10:", "codage pour toutes"[10])

# 18-19. Acronymes
print("\n18. Python pour tout le monde:", "".join([mot[0] for mot in "Python pour tout le monde".split()]))
print("19. Codage pour tous:", "".join([mot[0] for mot in societe.split()]))

# 20-22. Recherche caractères
print("\n20. Position de 'C':", "codage pour tous".find('c'))
print("21. Position de 'F':", "codage pour tous".find('F'))
print("22. Dernière 'L':", "codage pour tous".lower().rfind('l'))

# 23-27. Manipulation phrase
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print("\n23. Premier 'parce que':", phrase.find("parce que"))
print("24. Dernier 'parce que':", phrase.rindex("parce que"))
print("25. Découpage:", phrase[45:70])
print("26. Position premier 'parce que':", phrase.index("parce que"))
print("27. Découpage alternatif:", phrase[45:56+len("parce que")])

# 28-30. Vérifications
print("\n28. Commence par 'Coding':", "codage pour tous".startswith("Coding"))
print("29. Termine par 'coding':", "codage pour tous".endswith("coding"))
print("30. Strip:", "   codage pour tous   ".strip())

# 31. Identifiants
print("\n31. Identifiants valides:")
print("  30daysofpython:", "30daysofpython".isidentifier())
print("  Thirty_days_of_python:", "Thirty_days_of_python".isidentifier())

# 32. Jointure liste
bibliotheques = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("\n32.", " ".join(bibliotheques))

# 33. Saut de ligne
print("\n33. J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")

# 34. Tabulation
print("\n34. Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. Formatage cercle
rayon = 10
aire = 3.14 * rayon ** 2
print("\n35. La zone d'un cercle avec le rayon", rayon, "est de", aire, "mètres carrés.")

# 36. Opérations formatées
a, b = 8, 6
print("\n36. Opérations:")
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")