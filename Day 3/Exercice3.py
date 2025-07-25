# Exercice 1
age = 25  # Remplacez par votre âge

# Exercice 2
taille = 1.75  # en mètres

# Exercice 3
nombre_complexe = 3 + 4j

# Exercice 4
base = float(input("Entrez la base du triangle: "))
hauteur = float(input("Entrez la hauteur du triangle: "))
zone_triangle = 0.5 * base * hauteur
print("La zone du triangle est de", zone_triangle)

# Exercice 5
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre_triangle = a + b + c
print("Le périmètre du triangle est", perimetre_triangle)

# Exercice 6
longueur = float(input("Entrez la longueur du rectangle: "))
largeur = float(input("Entrez la largeur du rectangle: "))
surface = longueur * largeur
perimetre = 2 * (longueur + largeur)
print("Surface du rectangle:", surface)
print("Périmètre du rectangle:", perimetre)

# Exercice 7
pi = 3.14
r = float(input("Entrez le rayon du cercle: "))
aire_cercle = pi * r * r
circonference = 2 * pi * r
print("Aire du cercle:", aire_cercle)
print("Circonférence:", circonference)

# Exercice 8
x = 1
y = 2 * x - 2
print("Pour x =", x, ", y =", y)
pente = 2  # y = 2x - 2 → pente = 2

# Exercice 9
x1, y1 = 2, 2
x2, y2 = 6, 10
pente2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Pente entre (2,2) et (6,10):", pente2)
print("Distance euclidienne:", distance)

# Exercice 10
print("Les pentes sont-elles égales ?", pente == pente2)

# Exercice 11
x = -3
y = x ** 2 + 6 * x + 9
print("y =", y)

# Exercice 12
print(len("Python") != len("Dragon"))  # Falsy → False

# Exercice 13
print("on" in "python" and "on" in "dragon")  # True

# Exercice 14
phrase = "I hope this course is not full of jargon."
print("jargon" in phrase)  # True

# Exercice 15
print("on" not in "dragon" and "on" not in "python")  # False

# Exercice 16
texte = "python"
longueur = len(texte)
print("Longueur:", longueur)
print("Float:", float(longueur))
print("Str:", str(longueur))

# Exercice 17
nombre = int(input("Entrez un nombre: "))
print("Le nombre est pair ?", nombre % 2 == 0)

# Exercice 18
print(7 // 3 == int(2.7))  # True

# Exercice 19
print(type("10") == type(10))  # False

# Exercice 20
try:
    print(int('9.8') == 10)
except ValueError:
    print("Erreur : '9.8' ne peut pas être converti en int directement")

# Exercice 21
heures = float(input("Entrez les heures: "))
taux = float(input("Entrez le taux par heure: "))
gain = heures * taux
print("Votre gain hebdomadaire est de", gain)

# Exercice 22
annees = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = annees * 365 * 24 * 60 * 60
print("Vous avez vécu pendant", secondes, "secondes.")

# Exercice 23
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
