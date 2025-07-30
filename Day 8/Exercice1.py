# Day 8 - Dictionnaires en Python

# 1. Créer un dictionnaire vide appelé chien
chien = {}

# 2. Ajouter les infos dans le dictionnaire chien
chien['nom'] = 'Max'
chien['couleur'] = 'noir'
chien['race'] = 'Labrador'
chien['jambes'] = 4
chien['âge'] = 5
print("🐶 Dictionnaire chien :", chien)

# 3. Créer un dictionnaire étudiant
étudiant = {
    'first_name': 'Achraf',
    'last_name': 'Tcha-Tagba',
    'sexe': 'masculin',
    'âge': 25,
    'état_matrimonial': 'célibataire',
    'compétences': ['Python', 'HTML', 'CSS'],
    'pays': 'Togo',
    'ville': 'Lomé',
    'adresse': '123 Rue Exemple'
}
print("🎓 Dictionnaire étudiant :", étudiant)

# 4. Longueur du dictionnaire étudiant
print("📏 Longueur du dictionnaire étudiant :", len(étudiant))

# 5. Valeurs du dictionnaire comme une liste
valeurs = list(étudiant.values())
print("📋 Valeurs du dictionnaire étudiant :", valeurs)

# 6. Convertir en liste de tuples
tuples_etudiant = list(étudiant.items())
print("📦 Liste de tuples :", tuples_etudiant)

# 7. Supprimer un élément (ville)
étudiant.pop('ville')
print("🗑️ Étudiant après suppression de 'ville' :", étudiant)

# 8. Supprimer complètement le dictionnaire chien
del chien
print("✅ Le dictionnaire 'chien' a été supprimé.")
