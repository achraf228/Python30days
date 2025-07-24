# Jour 2: 30 Days of Python Programming

# ----------- NIVEAU 1 -----------

# 3 à 12. Déclarations de variables
prenom = "Achraf"
nom_de_famille = "Tcha-Tagba"
nom_complet = prenom + " " + nom_de_famille
pays = "Togo"
ville = "Lomé"
age = 27
est_marie = False
is_true = True
is_light_on = True

# 13. Déclaration multiple sur une seule ligne
x, y, z = 1, 2.5, "Python"

# ----------- NIVEAU 2 -----------

# 1. Vérification des types
print(type(prenom))
print(type(nom_de_famille))
print(type(nom_complet))
print(type(pays))
print(type(ville))
print(type(age))
print(type(est_marie))
print(type(is_true))
print(type(is_light_on))
print(type(x), type(y), type(z))

# 2. Longueur du prénom
print("Longueur du prénom :", len(prenom))

# 3. Comparaison des longueurs prénom vs nom de famille
print("Le prénom est plus long ?", len(prenom) > len(nom_de_famille))

# 4 à 10. Opérations avec num_one et num_two
num_one = 5
num_two = 4

somme = num_one + num_two
difference = num_one - num_two
produit = num_one * num_two
division = num_one / num_two
reste = num_two % num_one
floor_division = num_one // num_two

print("Somme:", somme)
print("Différence:", difference)
print("Produit:", produit)
print("Division:", division)
print("Reste:", reste)
print("Division entière (floor):", floor_division)

# 12. Aire et circonférence d’un cercle de rayon 30
import math

rayon = 30
area_of_circle = math.pi * rayon ** 2
circum_of_circle = 2 * math.pi * rayon

print("Aire du cercle:", area_of_circle)
print("Circonférence:", circum_of_circle)

# 12.Rayon saisi par l'utilisateur
rayon_user = float(input("Entrez un rayon (en mètres) : "))
aire_user = math.pi * rayon_user ** 2
print("Aire du cercle pour rayon saisi :", aire_user)

# 13. Entrée utilisateur
prenom_u = input("Prénom : ")
nom_u = input("Nom de famille : ")
pays_u = input("Pays : ")
age_u = input("Âge : ")
print(f"Bonjour {prenom_u} {nom_u}, {age_u} ans, de {pays_u}")

# 14. Liste des mots clés Python
# Tape ceci dans le shell Python :
# >>> help("keywords")

# Si on veux afficher depuis le fichier :
import keyword
print("Mots-clés réservés en Python :")
print(keyword.kwlist)
