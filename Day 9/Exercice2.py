# Exercice 1 : Notes des élèves
score = int(input("Entrez votre score: "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("Score invalide")

# Exercice 2 : Saison
mois = input("Entrez un mois: ").lower()

if mois in ["septembre", "octobre", "novembre"]:
    print("La saison est l'automne.")
elif mois in ["décembre", "janvier", "février"]:
    print("La saison est l'hiver.")
elif mois in ["mars", "avril", "mai"]:
    print("La saison est le printemps.")
elif mois in ["juin", "juillet", "août"]:
    print("La saison est l'été.")
else:
    print("Mois invalide.")

# Exercice 3 : Liste de fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Entrez le nom d’un fruit: ").lower()

if new_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(new_fruit)
    print("Liste mise à jour:", fruits)
