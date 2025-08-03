# Jour 12 - 30 Days of Python

import random
import string

# ====================
# NIVEAU 1
# ====================

# 1. Fonction pour générer un ID utilisateur aléatoire de 6 caractères
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

print("Exercice 1 :")
print(random_user_id())

# 2. Fonction qui génère plusieurs IDs avec une longueur et un nombre fournis par l'utilisateur
def user_id_gen_by_user():
    longueur = int(input("Entrez la longueur des IDs : "))
    nombre = int(input("Entrez le nombre d'IDs à générer : "))
    characters = string.ascii_letters + string.digits
    ids = [''.join(random.choices(characters, k=longueur)) for _ in range(nombre)]
    return ids

# Décommenter pour tester en direct
# print("Exercice 2 :")
# print(user_id_gen_by_user())

# 3. Fonction qui génère une couleur RGB aléatoire
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"RGB({r}, {g}, {b})"

print("Exercice 3 :")
print(rgb_color_gen())

# ====================
# NIVEAU 2
# ====================

# 1. Fonction qui renvoie une liste de couleurs hexadécimales
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        color = '#'+''.join(random.choices('0123456789ABCDEF', k=6))
        colors.append(color)
    return colors

print("Niveau 2 - Exercice 1 :")
print(list_of_hexa_colors(3))

# 2. Fonction qui renvoie une liste de couleurs RGB
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print("Niveau 2 - Exercice 2 :")
print(list_of_rgb_colors(3))

# 3. Fonction qui génère une liste de couleurs hexadécimales ou RGB
def generate_colors(type, n):
    if type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type de couleur non reconnu. Utilisez 'hexa' ou 'rgb'."

print("Niveau 2 - Exercice 3 :")
print(generate_colors('hexa', 2))
print(generate_colors('rgb', 2))

# ====================
# NIVEAU 3
# ====================

# 1. Fonction qui mélange une liste
def shuffle_list(liste):
    liste_copy = liste[:]
    random.shuffle(liste_copy)
    return liste_copy

print("Niveau 3 - Exercice 1 :")
print(shuffle_list([1, 2, 3, 4, 5]))

# 2. Fonction qui retourne 7 nombres aléatoires uniques entre 0 et 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print("Niveau 3 - Exercice 2 :")
print(unique_random_numbers())
