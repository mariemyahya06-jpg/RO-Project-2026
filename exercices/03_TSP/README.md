# Sujet 3 : Problème du voyageur de commerce, TSP

## Responsable
Nom : Maryeme Yahya Hourme
Numéro : C29782

## Idée du projet
Ce projet étudie le problème du voyageur de commerce, TSP.  
L’objectif général est de trouver un circuit de distance minimale.  
Pour la partie simplexe, on utilise une version linéaire simplifiée avec deux types de trajets.

## Hypothèses numériques

Les valeurs numériques utilisées dans ce sujet sont des données proposées pour construire un exemple simple et applicable.  
Le document du projet présente la description générale du problème, mais ne fournit pas toutes les données nécessaires à la résolution numérique.  
Ces valeurs permettent de formuler un exercice résoluble par la méthode du simplexe et de vérifier la solution avec Python.

## Variables de décision
- `X` : nombre de trajets effectués sur la route 1
- `Y` : nombre de trajets effectués sur la route 2

## Fonction objectif
Maximiser le gain de distance obtenu :

Z = 25X + 20Y

où :

- `25` représente le gain obtenu par le choix de la route 1
- `20` représente le gain obtenu par le choix de la route 2

## Contraintes
- X + Y <= 30  
- 4X + 2Y <= 100  
- 2X + 3Y <= 90  
- X >= 0  
- Y >= 0  

## Signification des contraintes
- `X + Y <= 30` : nombre maximal de trajets possibles
- `4X + 2Y <= 100` : contrainte de distance disponible
- `2X + 3Y <= 90` : contrainte de temps disponible

## Méthode utilisée
- Partie théorique : méthode du simplexe
- Implémentation : OR-Tools
- Solveur : moteur de routage OR-Tools

## Fichiers
- `distances.csv` : matrice des distances
- `model_ortools.py` : code Python avec OR-Tools
- `simplexe.tex` : exercice théorique avec la méthode du simplexe