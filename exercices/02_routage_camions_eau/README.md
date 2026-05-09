# Sujet 2 : Routage des camions d’eau

## Responsable
Nom : Fatimetou Mouhamed Lemin Saleh
Numéro : C25248

## Idée du projet
Ce projet étudie la planification des tournées de camions d’eau vers des quartiers périphériques.  
Pour la partie simplexe, on considère deux zones de distribution.

## Hypothèses numériques

Les valeurs numériques utilisées dans ce sujet sont des données proposées pour construire un exemple simple et applicable.  
Le document du projet présente la description générale du problème, mais ne fournit pas toutes les données nécessaires à la résolution numérique.  
Ces valeurs permettent de formuler un exercice résoluble par la méthode du simplexe et de vérifier la solution avec Python.

## Variables de décision
- `X` : nombre de tournées vers la zone 1
- `Y` : nombre de tournées vers la zone 2

## Fonction objectif
Maximiser la quantité d’eau distribuée :

Z = 30X + 40Y

où :

- `30` représente la quantité d’eau distribuée par une tournée vers la zone 1
- `40` représente la quantité d’eau distribuée par une tournée vers la zone 2

## Contraintes
- X + Y <= 50  
- 3X + 4Y <= 120  
- 2X + 5Y <= 150  
- X >= 0  
- Y >= 0  

## Signification des contraintes
- `X + Y <= 50` : nombre maximal de tournées possibles
- `3X + 4Y <= 120` : limite de carburant disponible
- `2X + 5Y <= 150` : limite de temps journalier disponible

## Méthode utilisée
- Partie théorique : méthode du simplexe
- Implémentation : OR-Tools
- Solveur : moteur de routage OR-Tools

## Fichiers
- `distances.csv` : matrice des distances
- `demands.csv` : demandes des points de distribution
- `model_ortools.py` : code Python avec OR-Tools
- `simplexe.tex` : exercice théorique avec la méthode du simplexe