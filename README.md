# 🧠 Algorithm Internship Test – GAP Time Correction

Ce repository présente une solution pour un **test de stage en algorithmique**, visant à développer un prototype de l’algorithme **GAP (Grade Adjusted Pace)**. Cet algorithme ajuste le temps de course en fonction du **dénivelé** rencontré lors d’un parcours.

---

## 📁 Contenu du Repository

| Fichier                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `script.py`            | Script Python principal : lit un fichier GPX, calcule distance/dénivelé, et corrige le pace. |
| `sample_course.gpx`    | Fichier GPX d'exemple représentant un parcours de 10 km.                    |
| `Documentation.md`     | Revue de littérature, choix méthodologiques, et suggestions d’amélioration. |

---

## ⚙️ Installation

### 1. Cloner le repository

Pour récupérer le repository, exécutez la commande suivante dans votre terminal :

```bash
git clone https://github.com/ZAKARIA-rgb-spaec/algorithm-internship-test.git
cd algorithm-internship-test

🚀 Utilisation
Une fois l'installation effectuée, vous pouvez exécuter le script en ligne de commande avec un fichier .gpx comme suit :

bash
Copier
Modifier
python script.py sample_course.gpx
🔧 Coefficient de Correction (optionnel)
Vous pouvez également spécifier un coefficient de correction k pour ajuster l'impact du dénivelé sur le pace. Par défaut, k vaut 0.03, mais vous pouvez modifier cette valeur si nécessaire :

bash
Copier
Modifier
python script.py sample_course.gpx 0.05
🔍 Exemple de sortie
Voici un exemple de sortie que vous obtiendrez après avoir exécuté le script avec un fichier GPX :

text
Copier
Modifier
Distance totale : 10.12 km  
Temps total : 52.43 minutes  
Pace moyen corrigé : 5.32 min/km
📌 Remarques
Le coefficient k permet d'ajuster l'effet du dénivelé sur le pace. La valeur par défaut est 0.03.

Le script traite les données GPX par segments, et pour chaque segment, il ajuste le pace en fonction de la pente rencontrée.



