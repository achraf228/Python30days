# =========================
# Jour 19 - Exercices Python
# =========================
import json
import re
from collections import Counter

# =========================
# NIVEAU 1
# =========================

# 1. Fonction qui compte le nombre de lignes et de mots dans un fichier texte
def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        mots = []
        for ligne in lignes:
            mots.extend(ligne.split())
        return len(lignes), len(mots)

# Test avec les fichiers donnés
fichiers_discours = [
    "data/obama_speech.txt",
    "data/michelle_obama_speech.txt",
    "data/donald_speech.txt",
    "data/melina_trump_speech.txt"
]

for fichier in fichiers_discours:
    lignes, mots = count_lines_and_words(fichier)
    print(f"{fichier} -> Lignes : {lignes}, Mots : {mots}")

# 2. Trouver les langues les plus parlées
def most_spoken_languages(file_name, top_n):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    langues = []
    for pays in data:
        langues.extend(pays.get('languages', []))
    compteur = Counter(langues)
    return compteur.most_common(top_n)

print("\nTop 10 langues :", most_spoken_languages("data/countries_data.json", 10))
print("Top 3 langues :", most_spoken_languages("data/countries_data.json", 3))

# 3. Les 10 pays les plus peuplés
def most_populated_countries(file_name, top_n):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data_sorted = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    return [{"country": p['name'], "population": p['population']} for p in data_sorted[:top_n]]

print("\nTop 10 pays :", most_populated_countries("data/countries_data.json", 10))
print("Top 3 pays :", most_populated_countries("data/countries_data.json", 3))

# =========================
# NIVEAU 2
# =========================

# 4. Extraire toutes les adresses e-mail
def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contenu = f.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', contenu)
    return list(set(emails))  # enlever doublons

emails = extract_emails("data/email_exchange_big.txt")
print(f"\nNombre d'emails trouvés : {len(emails)}")
print("Exemple :", emails[:10])

# 5. Mots les plus fréquents
def find_most_common_words(file_or_text, n):
    # Si c'est un fichier, on lit le contenu
    try:
        with open(file_or_text, 'r', encoding='utf-8') as f:
            texte = f.read()
    except FileNotFoundError:
        texte = file_or_text
    mots = re.findall(r'\w+', texte.lower())
    compteur = Counter(mots)
    return compteur.most_common(n)

print("\nTop 10 mots dans sample.txt :", find_most_common_words("data/sample.txt", 10))
print("Top 5 mots dans sample.txt :", find_most_common_words("data/sample.txt", 5))
