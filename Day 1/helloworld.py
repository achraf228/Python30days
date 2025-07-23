# Question 1: Afficher la version de Python (note : affichage manuel ici)
import sys
print("Python version:", sys.version)

# Question 2: operations mathématiques
print(3 + 4)  # Addition
print(3 - 4)  # Soustraction
print(3 * 4)  # Multiplication
print(3 % 4)  # Modulo
print(3 / 4)  # Division   
print(3 ** 4) # Puissance
print(3 // 4) # Division entière
# Question 3: Chaine de caractères
print("Achraf")  
print("Tcha-Tagba")
print("TOGO")
print("Je profite de 30jours de python")
# Question 4: verifier le type de données
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finlande']))
print(type("Achraf"))
print(type("Tcha-Tagba"))
print(type("TOGO"))

# Exercice 2
# Question 1: Afficher le type de données
entier = 34
float = 3.14
complexe = 4 - 4j


#String
chaine = "Achraf"

#booléen
booleen = False

#Liste
liste = ['Achraf', 'Tcha-Tagba', 'TOGO']

#tuple
tuple = ('Achraf', 'Tcha-Tagba', 'TOGO')

#ensemble
set = {'Achraf', 'Tcha-Tagba', 'TOGO'}

#dictionnaire
dictionnaire = {
    "Nom": 'Achraf', "Prenom": 'Tcha-Tagba', "Pays": 'TOGO'}

#verifier le type de données
print(type(entier), entier)
print(type(float), float)
print(type(complexe), complexe)
print(type(chaine), chaine)
print(type(booleen), booleen)
print(type(liste), liste)
print(type(tuple), tuple)
print(type(set), set)
print(type(dictionnaire), dictionnaire)
 
# Question 2: calcul distance euclidienne
import math
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance euclidienne:", distance)    