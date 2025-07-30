# Données
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convertir en set et comparer longueurs
age_set = set(age)
print("1: Longueur liste =", len(age), ", Longueur set =", len(age_set))
# Le set est plus petit car il ne garde que les valeurs uniques

# 2. Différences entre :
# - Chaîne (str) : texte, ex. "Bonjour"
# - Liste (list) : collection ordonnée et modifiable, ex. [1, 2, 3]
# - Tuple (tuple) : collection ordonnée et immuable, ex. (1, 2, 3)
# - Set (set) : collection non ordonnée, sans doublons, ex. {1, 2, 3}

# 3. Compter les mots uniques
phrase = "I am a teacher and I love to inspire and teach people"
mots = phrase.split()
mots_uniques = set(mots)
print("3:", mots_uniques)
print("Nombre de mots uniques :", len(mots_uniques))
