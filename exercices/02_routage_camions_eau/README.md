# Sujet 2 : Routage des camions d'eau

## Responsable
- **Nom :** Fatimetou Mohamed Lemin Saleh
- **Numéro :** C25248

## Idée du projet
Planifier les tournées des camions d'eau vers deux zones de distribution afin de maximiser la quantité totale d'eau distribuée, tout en respectant les contraintes de ressources (nombre de tournées, capacité, temps).

## Données utilisées
- `distribution_eau_data.csv`

## Variables de décision
- `X` : nombre de tournées vers la zone 1
- `Y` : nombre de tournées vers la zone 2

## Fonction objectif
Maximiser la quantité totale d'eau distribuée :

```
Zmax = 30X + 40Y
```

## Contraintes
```
X + Y    <= 50
3X + 4Y  <= 120
2X + 5Y  <= 150
X >= 0,  Y >= 0
```

## Méthodes utilisées
- **Partie théorique :** méthode du simplexe
- **Implémentation :** OR-Tools Linear Solver (GLOP)

## Résultat attendu
Le problème admet **deux solutions optimales équivalentes** donnant la même valeur de Z :

```
Solution 1 :  X = 40,   Y = 0
Solution 2 :  X = 0,    Y = 30
Zmax = 1200
```
Dans les deux cas, la quantité totale d'eau distribuée est de 1200 unités. La société peut choisir l'organisation qui convient le mieux aux conditions du terrain.

## Fichiers
- `README.md` : ce document
- `distribution_eau_data.csv` : données du modèle (variables, coefficients, contraintes)
- `model_ortools.py` : modèle PL résolu avec OR-Tools (GLOP)
- `simplexe.tex` : exercice théorique résolu par la méthode du simplexe
- `simplexe.pdf` : version compilée du fichier LaTeX
