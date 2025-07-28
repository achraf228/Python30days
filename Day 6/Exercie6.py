# 1. tuple vide
tuple_vide = ()

# 2. Tuple contenant les noms des frères et sœurs imaginaires
brothers = ("Hidre", "Mike", "Alex")
sisters = ("Anna", "Farida", "Yasmine")

# 3. Rejoignez les deux tuples
deux_tuple = brothers + sisters

# 4. Nombre total de frères et sœurs
print("Nombre de frères et sœurs :", len(deux_tuple))
# 5. Ajout des parents
family_members = deux_tuple + ("Papa", "Maman")
print("Membres de la famille :", family_members)

#Exercice 2
# 1. Déballer les membres de la famille
*freres_soeurs, pere, mere = family_members
print("Frères et sœurs :", freres_soeurs)
print("Père :", pere)
print("Mère :", mere)

# 2. Tuples de fruits, légumes, produits animaux
fruits = ("pomme", "banane", "orange")
vegetables = ("carotte", "tomate", "laitue")
animal_products = ("lait", "œuf", "fromage")

# Rejoindre tous les tuples
tuple_complet = fruits + vegetables + animal_products
print("Tuple des aliments :", tuple_complet)

# 3. Convertir le tuple en liste
tuple_complet = list(tuple_complet)
print("Liste des aliments :", tuple_complet)

# 4. Extraire l'article ou les articles du milieu
middle_index = len(tuple_complet) // 2
if len(tuple_complet) % 2 == 0:
    print("Articles du milieu :", tuple_complet[middle_index - 1: middle_index + 1])
else:
    print("Article du milieu :", tuple_complet[middle_index])

# 5. Slice des 3 premiers et 3 derniers éléments
print("3 premiers éléments :", tuple_complet[:3])
print("3 derniers éléments :", tuple_complet[-3:])

# 6. Supprimer complètement le tuple food_stuff_tp
del tuple_complet
# print(food_stuff_tp)  # Provoquera une erreur si tu décommente car le tuple est supprimé

# 7. Vérifier si un élément est dans un tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonie est un pays nordique ?", 'Estonie' in nordic_countries)
print("Iceland est un pays nordique ?", 'Iceland' in nordic_countries)
