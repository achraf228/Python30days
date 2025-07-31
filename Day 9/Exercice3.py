personne = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'zipcode': '02210'
}

# Vérifier s’il y a des compétences
if 'skills' in personne:
    skills = personne['skills']
    mid_index = len(skills) // 2
    print("Compétence(s) du milieu:", skills[mid_index])

    # Vérifier si Python est présent
    if 'Python' in skills:
        print("La personne a des compétences en Python.")

    # Vérifier le type de développeur
    if skills == ['JavaScript', 'React']:
        print("Il est un développeur frontend.")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("Il est un développeur backend.")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("Il est un développeur fullstack.")
    else:
        print("Inconnu.")
else:
    print("Aucune compétence trouvée.")

# Vérifier état civil et pays
if personne['is_married'] and personne['country'] == 'Finland':
    print(f"{personne['first_name']} {personne['last_name']} vit en Finlande. Il est marié.")
