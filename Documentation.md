
```markdown
# Documentation du Projet - Algorithm Internship Test

## 1. Revue de la Littérature et Approches

Plusieurs approches ont été étudiées pour ajuster le temps de course en fonction du dénivelé :
- **Méthode GAP de Strava** : Ajustement basé sur une approche reverse-engineered.
- **Daniels’ Running Formula** : Utilisation des VDOT tables pour évaluer l'effort.
- **Modèles basés sur la science de l'effort** : Exemple, Minetti (2002) qui étudie le coût énergétique des pentes.
- **Approches par machine learning** : Modèles statistiques prenant en compte plusieurs paramètres.

## 2. Sélection de la Méthode

Pour ce prototype, nous avons sélectionné une méthode simple basée sur un facteur de correction proportionnel au grade de la montée/descente.

La formule appliquée est :
corrected_pace = actual_pace * (1 + k * grade)
markdown
Copier
où `k` est un coefficient empirique (ici fixé à 0,03).

Cette approche présente l'avantage d'être simple à implémenter et facilement testable avec des données GPS.

## 3.Pourquoi ce choix ?
•	Simplicité d’implémentation
Cette méthode demande un calcul simple (multiplication et addition) qui permet de transformer directement le rythme réel à partir d’un facteur de correction. Elle est aisée à coder et à valider rapidement dans un environnement de test.
•	Lisibilité et transparence
La relation linéaire entre la montée (ou descente) et le pace facilite la compréhension de l’impact de chaque variation de dénivelé sur la performance. Cela permet d’expliquer clairement le fonctionnement de l’algorithme à des collaborateurs ou des recruteurs.
•	Adaptabilité aux données disponibles
Les données extraites d’un fichier GPX (latitude, longitude, altitude et timestamp) suffisent pour appliquer cette correction. On n’a pas besoin d’informations supplémentaires complexes pour mettre en œuvre ce modèle.


## 4. Description du Prototype

Le script Python réalise les opérations suivantes :
1. **Lecture du fichier GPX** pour extraire les points GPS (latitude, longitude, altitude, temps).
2. **Calcul de la distance** parcourue entre chaque point en utilisant la formule haversine.
3. **Calcul du grade** (dénivelé relatif) pour chaque segment.
4. **Calcul du pace** (temps en minutes par kilomètre) pour chaque segment.
5. **Application de la correction** en utilisant la formule définie.

## 5. Perspectives d'Amélioration

- Intégrer des paramètres environnementaux (température, humidité).
- Adapter la correction en fonction des caractéristiques individuelles (VO2 max, seuil lactique, etc.).
- Tester et valider l'algorithme sur d'autres parcours et avec des données réelles.

