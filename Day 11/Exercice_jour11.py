import math
from collections import Counter
from statistics import mean, median, mode, variance, stdev

# ------------------- Niveau 1 -------------------

# 1. Addition de deux nombres
def add_two_numbers(a, b):
    return a + b

# 2. Aire d'un cercle
def area_of_circle(r):
    return math.pi * r * r

# 3. Addition de tous les nombres (avec vérification type)
def add_all_nums(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        return "Tous les éléments doivent être des nombres."
    return sum(args)

# 4. Conversion Celsius -> Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5. Check saison selon mois
def check_season(month):
    month = month.lower()
    if month in ['décembre', 'janvier', 'février']:
        return "hiver"
    elif month in ['mars', 'avril', 'mai']:
        return "printemps"
    elif month in ['juin', 'juillet', 'août']:
        return "été"
    elif month in ['septembre', 'octobre', 'novembre']:
        return "automne"
    else:
        return "Mois invalide"

# 6. Calcul pente d'une droite (y = mx + b), slope = (y2 - y1)/(x2 - x1)
def calcul_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pente infinie (division par zéro)"
    return (y2 - y1) / (x2 - x1)

# 7. Résoudre équation quadratique ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Pas de solution réelle"
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)

# 8. Imprimer les éléments d'une liste
def print_list(lst):
    for elem in lst:
        print(elem)

# 9. Inverser une liste avec boucle
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Mettre en majuscule les éléments d'une liste
def capitalize_list_items(lst):
    return [str(item).upper() for item in lst]

# 11. Ajouter un élément à la liste
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Supprimer un élément de la liste
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Somme des nombres de 0 à n
def sum_of_numbers(n):
    return sum(range(n+1))

# 14. Somme des nombres impairs de 0 à n
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

# 15. Somme des nombres pairs de 0 à n
def sum_of_evens(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

# ------------------- Niveau 2 -------------------

# 1. Compter pairs et impairs dans un nombre donné
def evens_and_odds(n):
    evens = len([i for i in range(n+1) if i % 2 == 0])
    odds = len([i for i in range(n+1) if i % 2 != 0])
    print(f"Le nombre de cotes est de {odds}.")
    print(f"Le nombre d'Evens est de {evens}.")

# 2. Calculer factorielle
def factorielle(n):
    if n < 0:
        return "Le nombre doit être positif"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 3. Vérifier si variable est vide
def is_empty(var):
    if var:
        return False
    else:
        return True

# 4. Fonctions statistiques sur liste

def calculer_mean(lst):
    return mean(lst)

def calculer_median(lst):
    return median(lst)

def calculer_mode(lst):
    try:
        return mode(lst)
    except:
        return "Pas de mode unique"

def calculer_range(lst):
    return max(lst) - min(lst)

def calculer_variance(lst):
    return variance(lst)

def calculer_std(lst):
    return stdev(lst)

# ------------------- Niveau 3 -------------------

# 1. Vérifier si un nombre est premier
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

# 2. Vérifier si tous les éléments d'une liste sont uniques
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Vérifier si tous les éléments sont du même type
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(x, first_type) for x in lst)

# 4. Vérifier si une variable est un nom de variable Python valide
def is_valid_variable(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

# 5. Fonctions fictives en attente d'accès aux fichiers Pays-data.py
def les_plus_parlees_langues():
    # Exemple statique
    return ["Mandarin", "Espagnol", "Anglais", "Hindi", "Arabe", "Bengali", "Portugais", "Russe", "Japonais", "Lahnda"]

def les_plus_populees_pays():
    # Exemple statique
    return ["Chine", "Inde", "États-Unis", "Indonésie", "Pakistan", "Brésil", "Nigeria", "Bangladesh", "Russie", "Mexique"]

# Exemple d'utilisation
if __name__ == "__main__":
    print("Add two numbers:", add_two_numbers(3, 5))
    print("Area of circle (r=5):", area_of_circle(5))
    print("Add all nums:", add_all_nums(1, 2, 3, 4))
    print("Convert 0°C to F:", convert_celsius_to_fahrenheit(0))
    print("Check season (mars):", check_season("mars"))
    print("Slope between (1,2) and (3,4):", calcul_slope(1, 2, 3, 4))
    print("Solve quadratic (1, -3, 2):", solve_quadratic_eqn(1, -3, 2))
    print("Reverse list:", reverse_list([1, 2, 3, 4, 5]))
    print("Capitalize list items:", capitalize_list_items(['a', 'b', 'c']))
    print("Add item:", add_item(['apple', 'banana'], 'cherry'))
    print("Remove item:", remove_item(['apple', 'banana', 'cherry'], 'banana'))
    print("Sum of numbers (5):", sum_of_numbers(5))
    print("Sum of odds (10):", sum_of_odds(10))
    print("Sum of evens (10):", sum_of_evens(10))
    evens_and_odds(100)
    print("Factorial (5):", factorielle(5))
    print("Is empty []:", is_empty([]))
    print("Is 7 prime:", is_prime(7))
    print("All unique [1,2,3]:", all_unique([1, 2, 3]))
    print("All same type [1, 2, 3]:", all_same_type([1, 2, 3]))
    print("Is valid variable 'var1':", is_valid_variable("var1"))
    print("Top spoken languages:", les_plus_parlees_langues())
    print("Top populated countries:", les_plus_populees_pays())
