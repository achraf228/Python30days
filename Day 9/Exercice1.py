# Exercice 1
age = int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes assez vieux pour apprendre à conduire.")
else:
    reste = 18 - age
    print(f"Vous avez besoin de {reste} ans de plus pour apprendre à conduire.")

# Exercice 2
my_age = 25
your_age = int(input("Entrez votre âge: "))

diff = abs(my_age - your_age)

if your_age > my_age:
    if diff == 1:
        print("Vous avez 1 an de plus que moi.")
    else:
        print(f"Vous avez {diff} ans de plus que moi.")
elif your_age < my_age:
    if diff == 1:
        print("J'ai 1 an de plus que vous.")
    else:
        print(f"J'ai {diff} ans de plus que vous.")
else:
    print("Nous avons le même âge.")

# Exercice 3
a = int(input("Entrez le premier numéro: "))
b = int(input("Entrez le deuxième numéro: "))

if a > b:
    print(f"{a} est supérieur à {b}")
elif a < b:
    print(f"{a} est plus petit que {b}")
else:
    print(f"{a} est égal à {b}")
