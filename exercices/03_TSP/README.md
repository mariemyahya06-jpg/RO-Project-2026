# Sujet 3 : Problème du voyageur de commerce (TSP)

## Responsable
- **Nom :** Maryem Yahya Hourme
- **Numéro :** C29782

## Idée du projet
Étudier une version linéaire simplifiée du problème du voyageur de commerce, dans laquelle on choisit entre deux types de trajets afin de maximiser le gain total tout en respectant les contraintes de ressources.

## Données utilisées
- `tsp_data.csv`

## Variables de décision
- `X` : nombre de trajets effectués sur la route 1
- `Y` : nombre de trajets effectués sur la route 2

## Fonction objectif
Maximiser le gain obtenu :

```
Zmax = 25X + 20Y
```

## Contraintes
```
X + Y    <= 30
4X + 2Y  <= 100
2X + 3Y  <= 90
X >= 0,  Y >= 0
```

## Méthodes utilisées
- **Partie théorique :** méthode du simplexe
- **Implémentation :** OR-Tools Linear Solver (GLOP)

## Résultat attendu
```
X = 20,   Y = 10
Zmax = 700
```
La meilleure combinaison consiste à effectuer 20 trajets sur la route 1 et 10 trajets sur la route 2. Le gain maximal obtenu est de 700 unités.

## Fichiers
- `README.md` : ce document
- `tsp_data.csv` : données du modèle (variables, coefficients, contraintes)
- `model_ortools.py` : modèle PL résolu avec OR-Tools (GLOP)
- `simplexe.tex` : exercice théorique résolu par la méthode du simplexe
- `simplexe.pdf` : version compilée du fichier LaTeX
