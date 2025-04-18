# Algorithm Internship Test - GAP Time Correction

Ce repository contient la solution du test de stage pour développer un prototype d'algorithme GAP (Grade Adjusted Pace) qui ajuste le temps de course en fonction du dénivelé.

## Contenu du Repository

- **Documentation.md** : Document expliquant la revue de littérature, le choix méthodologique, et les pistes d'amélioration.
- **script.py** : Script Python qui lit un fichier GPX, calcule la distance et le dénivelé, puis corrige le pace.
- **sample_course.gpx** : Fichier GPX d'exemple représentant un parcours 10K.

## Installation

1. Cloner le repository :
   ```bash
   git clone https://github.com/votre-nom/algorithm-internship-test.git
   cd algorithm-internship-test
2.	Installer les dépendances (par exemple, la bibliothèque gpxpy) :
bash
Copier
pip install gpxpy
Utilisation
Pour tester le prototype, exécutez la commande suivante en indiquant le fichier GPX d'exemple :
bash
Copier
python script.py sample_course.gpx
Le script affichera la distance totale, le temps total et le pace moyen corrigé.
Perspectives d'Amélioration
•	Intégrer des données environnementales (température, humidité).
•	Adapter l'algorithme aux paramètres individuels (VO2 max, seuil lactique, etc.).
•	Explorer des méthodes avancées (machine learning, modélisation physique plus fine).

