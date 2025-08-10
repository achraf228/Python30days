# =========================
# Jour 16 - Exercices Python
# =========================

from datetime import datetime, date

# 1. Obtenir le jour, mois, année, heure, minute et horodatage
now = datetime.now()
print("Jour   :", now.day)
print("Mois   :", now.month)
print("Année  :", now.year)
print("Heure  :", now.hour)
print("Minute :", now.minute)
print("Horodatage :", now.timestamp())

# 2. Formater la date actuelle
formatted_date = now.strftime("%m/%d/%y, %H:%M:%S")
print("Date formatée :", formatted_date)

# 3. Changer une date donnée
given_date = datetime(2019, 12, 5)
print("Date donnée :", given_date)
new_date = given_date.replace(year=2025, month=8, day=10)
print("Date modifiée :", new_date)

# 4. Décalage jusqu'au Nouvel An
new_year = datetime(now.year + 1, 1, 1)
delta_new_year = new_year - now
print("Jours jusqu'au Nouvel An :", delta_new_year.days)
print("Heures restantes :", delta_new_year.seconds // 3600)

# 5. Décalage entre le 1er janvier 1970 et maintenant
epoch = datetime(1970, 1, 1)
delta_epoch = now - epoch
print("Nombre de jours depuis 1970 :", delta_epoch.days)
print("Nombre total de secondes depuis 1970 :", delta_epoch.total_seconds())

# 6. Pourquoi utiliser le module datetime ?
raisons = [
    "Analyse des séries chronologiques",
    "Obtenir un horodatage de toutes les activités dans une application",
    "Ajouter automatiquement la date aux articles d’un blog"
]
print("\nPourquoi utiliser datetime ?")
for r in raisons:
    print("-", r)
