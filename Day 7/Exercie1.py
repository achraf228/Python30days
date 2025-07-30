# Données
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Longueur de l'ensemble
print("1:", len(it_companies))

# 2. Ajouter 'Twitter'
it_companies.add('Twitter')
print("2:", it_companies)

# 3. Ajouter plusieurs entreprises
it_companies.update(['Tesla', 'Samsung', 'Intel'])
print("3:", it_companies)

# 4. Supprimer une entreprise (ex: 'IBM')
it_companies.remove('IBM')
print("4:", it_companies)

# 5. Différence entre remove et discard
# - `remove()` : génère une erreur si l'élément n'existe pas
# - `discard()` : ne génère pas d'erreur si l'élément n'existe pas
