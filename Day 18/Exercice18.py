# =========================
# Jour 18 - Exercices Python
# =========================

from collections import Counter
import re

# =========================
# NIVEAU 1
# =========================

# 1. Trouver le mot le plus fréquent
paragraphe = """J'adore enseigner. Si vous n'aimez pas enseigner ce que vous pouvez aimer d'autre.
J'adore Python si vous n'aimez pas quelque chose qui peut vous donner toutes les capacités
de développer une application que pouvez-vous aimer d'autre."""

mots = re.findall(r'\w+', paragraphe.lower())
compteur = Counter(mots)
plus_frequents = compteur.most_common()
print("Niveau 1 - Mots les plus fréquents :", plus_frequents)

# 2. Distance entre les deux particules les plus éloignées
points = [-12, -4, -3, -1, 0, 4, 8]
distance = max(points) - min(points)
print("Niveau 1 - Distance :", distance)

# =========================
# NIVEAU 2
# =========================

def is_valid_variable(nom):
    return re.match(r'^[a-zA-Z_]\w*$', nom) is not None

print("Niveau 2 - Variable valide ?")
print("first_name   :", is_valid_variable('first_name'))   # True
print("premier-nom  :", is_valid_variable('premier-nom'))  # False
print("1First_name  :", is_valid_variable('1First_name'))  # False
print("firstname    :", is_valid_variable('firstname'))    # True

# =========================
# NIVEAU 3
# =========================

phrase = """%i$ am @% a% tea @ cher%, && i lo% # ve% tea @ ching%;.
Il n'y a rien; & as & mo @ re-récompense comme educa @ ting &&& @ emp% o @ wering peo @ ple.
; J'ai trouvé le thé @ ching m% o @ re intéressant tha @ n tout autre% jo @ bs.
% Do @ es thi% s mo @ tivate yo @ u pour être un thé @ cher !?"""

def clean_text(text):
    texte_nettoye = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ\s]', '', text)
    return texte_nettoye.lower()

def most_frequent_words(text, n=3):
    mots = text.split()
    compteur = Counter(mots)
    return compteur.most_common(n)

cleaned = clean_text(phrase)
top3 = most_frequent_words(cleaned, 3)

print("Niveau 3 - Texte nettoyé :", cleaned)
print("Niveau 3 - Top 3 mots :", top3)
