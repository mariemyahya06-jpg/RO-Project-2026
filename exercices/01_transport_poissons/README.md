# Sujet 1 : Transport de poissons Nouadhibou–Nouakchott

## Responsable
Nom : Sara Rabani
Numéro : C30911

## Idée du projet
Ce projet étudie l’organisation du transport du poisson frais entre Nouadhibou et Nouakchott.  
On considère deux types de destinations : le marché principal et les restaurants/supermarchés.

## Hypothèses numériques

Les valeurs numériques utilisées dans ce sujet sont des données proposées pour construire un exemple simple et applicable.  
Le document du projet présente la description générale du problème, mais ne fournit pas toutes les données nécessaires à la résolution numérique.  
Ces valeurs permettent de formuler un exercice résoluble par la méthode du simplexe et de vérifier la solution avec Python.

## Variables de décision
- `X` : quantité de poisson transportée vers le marché principal
- `Y` : quantité de poisson transportée vers les restaurants et supermarchés

## Fonction objectif
Maximiser le bénéfice total du transport :

Z = 40X + 50Y

où :

- `40` représente le bénéfice unitaire pour le marché principal
- `50` représente le bénéfice unitaire pour les restaurants et supermarchés

## Contraintes
- X + Y <= 100  
- 2X + 3Y <= 240  
- X + 2Y <= 160  
- X >= 0  
- Y >= 0  

## Signification des contraintes
- `X + Y <= 100` : quantité totale de poisson disponible
- `2X + 3Y <= 240` : temps total de transport disponible
- `X + 2Y <= 160` : capacité de conservation frigorifique

## Méthode utilisée
- Partie théorique : méthode du simplexe
- Implémentation : Pyomo
- Solveur : GLPK

## Fichiers
- `data.csv` : données du problème
- `model_pyomo.py` : code Python avec Pyomo
- `simplexe.tex` : exercice théorique avec la méthode du simplexe