# Sujet 1 : Transport de poissons Nouadhibou – Nouakchott

## Responsable
- **Nom :** Sara Rabani
- **Numéro :** C30911

## Idée du projet
Organiser le transport du poisson frais entre Nouadhibou (centre de pêche) et Nouakchott (centre de consommation) afin de maximiser le bénéfice total, tout en respectant les capacités de transport et de conservation.

## Données utilisées
- `transport_poissons_data.csv`

## Variables de décision
- `X` : quantité de poisson transportée vers le marché principal
- `Y` : quantité de poisson transportée vers les restaurants et supermarchés

## Fonction objectif
Maximiser le bénéfice total :

```
Zmax = 40X + 50Y
```

## Contraintes
```
X + Y    <= 100
2X + 3Y  <= 240
X + 2Y   <= 160
X >= 0,  Y >= 0
```

## Méthodes utilisées
- **Partie théorique :** méthode du simplexe
- **Implémentation :** Pyomo + GLPK

## Résultat attendu
```
X = 60,   Y = 40
Zmax = 4400
```
L'entreprise transporte 60 unités vers le marché principal et 40 unités vers les restaurants/supermarchés. Le bénéfice maximal obtenu est de 4400 unités.

## Fichiers
- `README.md` : ce document
- `transport_poissons_data.csv` : données du modèle (variables, coefficients, contraintes)
- `model_pyomo.py` : modèle PL résolu avec Pyomo + GLPK
- `simplexe.tex` : exercice théorique résolu par la méthode du simplexe
- `simplexe.pdf` : version compilée du fichier LaTeX
