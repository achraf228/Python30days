import requests
from collections import Counter
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

def exercice1():
    print("\n=== Exercice 1: Analyse de Romeo and Juliet ===")
    try:
        # Télécharger le texte
        response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
        text = response.text

        # Nettoyer et compter les mots (en excluant le header et footer du projet Gutenberg)
        start = text.find("ROMEO AND JULIET")
        end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
        content = text[start:end] if start != -1 and end != -1 else text

        words = re.findall(r'\b\w+\b', content.lower())
        word_counts = Counter(words)

        # Exclure les mots courts non significatifs
        common_words = {'the', 'and', 'to', 'of', 'i', 'a', 'in', 'that', 'is', 'it', 
                       'you', 'he', 'this', 'for', 'my', 'with', 'not', 'him', 'me', 'your'}
        filtered_counts = {word: count for word, count in word_counts.items() 
                          if word not in common_words and len(word) > 3}

        # Top 10 des mots les plus fréquents
        top_10 = Counter(filtered_counts).most_common(10)
        print("Top 10 des mots les plus fréquents (hors mots communs):")
        for word, count in top_10:
            print(f"{word}: {count}")
    except Exception as e:
        print(f"Erreur dans l'exercice 1: {e}")

def exercice2():
    print("\n=== Exercice 2: Analyse de l'API Cats ===")
    try:
        # Récupérer les données
        cats_data = requests.get('https://api.thecatapi.com/v1/breeds').json()

        # i. Statistiques sur le poids
        weights = []
        for cat in cats_data:
            if 'weight' in cat and 'metric' in cat['weight']:
                weight_str = cat['weight']['metric'].replace(' - ', '-').split('-')
                try:
                    avg_weight = (float(weight_str[0]) + float(weight_str[1]))/2
                    weights.append(avg_weight)
                except:
                    pass

        print("\nStatistiques poids (kg):")
        print(f"Min: {np.min(weights):.2f}, Max: {np.max(weights):.2f}")
        print(f"Moyenne: {np.mean(weights):.2f}, Médiane: {np.median(weights):.2f}")
        print(f"Écart-type: {np.std(weights):.2f}")

        # ii. Statistiques sur la durée de vie
        lifespans = []
        for cat in cats_data:
            if 'life_span' in cat:
                lifespan_str = cat['life_span'].replace(' - ', '-').split('-')
                try:
                    avg_life = (float(lifespan_str[0]) + float(lifespan_str[1]))/2
                    lifespans.append(avg_life)
                except:
                    pass

        print("\nStatistiques durée de vie (années):")
        print(f"Min: {np.min(lifespans):.2f}, Max: {np.max(lifespans):.2f}")
        print(f"Moyenne: {np.mean(lifespans):.2f}, Médiane: {np.median(lifespans):.2f}")
        print(f"Écart-type: {np.std(lifespans):.2f}")

        # iii. Table de fréquence
        df = pd.DataFrame(cats_data)
        freq_table = df.groupby(['origin', 'name']).size().unstack(fill_value=0)
        print("\nTable de fréquence (extrait):")
        print(freq_table.iloc[:5, :5])  # Afficher seulement les 5 premières lignes et colonnes
    except Exception as e:
        print(f"Erreur dans l'exercice 2: {e}")

def exercice3():
    print("\n=== Exercice 3: API des pays ===")
    try:
        # Récupérer les données des pays (version v3.1 de l'API)
        countries_data = requests.get('https://restcountries.com/v3.1/all').json()

        # i. 10 plus grands pays par superficie
        valid_countries = [c for c in countries_data if 'area' in c and isinstance(c['area'], (int, float))]
        sorted_countries = sorted(valid_countries, key=lambda x: x['area'], reverse=True)
        
        print("\n10 plus grands pays:")
        for i, country in enumerate(sorted_countries[:10], 1):
            name = country['name']['common'] if 'name' in country and 'common' in country['name'] else 'Inconnu'
            area = country.get('area', 'N/A')
            print(f"{i}. {name}: {area} km²")

        # ii. 10 langues les plus parlées
        lang_count = {}
        for country in countries_data:
            if 'languages' in country and 'population' in country:
                for lang_code, lang_name in country['languages'].items():
                    lang_count[lang_name] = lang_count.get(lang_name, 0) + country['population']

        sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
        print("\n10 langues les plus parlées:")
        for i, (lang, pop) in enumerate(sorted_langs[:10], 1):
            print(f"{i}. {lang}: ~{pop//1_000_000} millions de locuteurs")

        # iii. Nombre total de langues
        print(f"\nNombre total de langues: {len(lang_count)}")
    except Exception as e:
        print(f"Erreur dans l'exercice 3: {e}")

def exercice4():
    print("\n=== Exercice 4: Analyse UCI avec BeautifulSoup ===")
    try:
        url = 'https://archive.ics.uci.edu/ml/datasets.php'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trouver la table des datasets
        datasets_table = soup.find('table', {'border': '1'})
        if datasets_table:
            datasets = datasets_table.find_all('tr')[1:]  # Ignorer l'en-tête
            
            print("\n5 premiers datasets UCI:")
            for dataset in datasets[:5]:
                cells = dataset.find_all('td')
                if len(cells) >= 2:
                    name = cells[0].get_text(strip=True)
                    print(f"- {name}")
        else:
            print("La structure de la page a changé, impossible de trouver la table des datasets")
    except Exception as e:
        print(f"Erreur dans l'exercice 4: {e}")

def main():
    print("=== Début des exercices ===")
    
    # Exécution des exercices
    exercice1()
    exercice2()
    exercice3()
    exercice4()
    
    print("\n=== Fin des exercices ===")

if __name__ == "__main__":
    main()