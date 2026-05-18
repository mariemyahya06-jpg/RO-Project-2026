# Projet de Recherche Opérationnelle 2026

Ce projet présente la résolution de **trois problèmes d'optimisation linéaire** en Recherche Opérationnelle, modélisés et résolus à la fois théoriquement (méthode du simplexe) et informatiquement (Python).

## Membres du groupe

| Nom | Numéro |
|---|---|
| Sara Rabani | C30911 |
| Fatimetou Mohamed Lemin Saleh | C25248 |
| Maryem Yahya Hourme | C29782 |

**Année universitaire :** 2025–2026

## Objectif du projet

L'objectif est de modéliser et résoudre trois problèmes d'optimisation sous forme de programmes linéaires à deux variables \(X\) et \(Y\). Pour chaque sujet, le même modèle est résolu :

- **Théoriquement** par la méthode du simplexe (fichier `simplexe.tex`)
- **Informatiquement** en Python (Pyomo + GLPK pour le Sujet 1, OR-Tools Linear Solver pour les Sujets 2 et 3)

Chaque sujet repose sur **un seul fichier CSV** qui regroupe les variables, les coefficients de la fonction objectif et les contraintes.

## Outils utilisés

- **Python** — implémentation des modèles
- **Pyomo** — modélisation linéaire (Sujet 1)
- **GLPK** — solveur linéaire utilisé avec Pyomo
- **OR-Tools Linear Solver (GLOP)** — Sujets 2 et 3
- **LaTeX** — rédaction du rapport et des exercices simplexe
- **GitHub** — organisation et partage du projet

## Structure du projet

```text
RO-Project-2026/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── rapport/
│   ├── main.tex
│   ├── main.pdf
│   └── references.bib
│
├── presentation/
│   └── README.md
│
└── exercices/
    ├── 01_transport_poissons/
    │   ├── transport_poissons_data.csv
    │   ├── model_pyomo.py
    │   ├── simplexe.tex
    │   ├── simplexe.pdf
    │   └── README.md
    │
    ├── 02_routage_camions_eau/
    │   ├── distribution_eau_data.csv
    │   ├── model_ortools.py
    │   ├── simplexe.tex
    │   ├── simplexe.pdf
    │   └── README.md
    │
    └── 03_TSP/
        ├── tsp_data.csv
        ├── model_ortools.py
        ├── simplexe.tex
        ├── simplexe.pdf
        └── README.md
```

## Description des trois sujets

### Sujet 1 — Transport de poissons (Nouadhibou ↔ Nouakchott)
- **Responsable :** Sara Rabani (C30911)
- **Données :** `transport_poissons_data.csv`
- **Modèle :** `Zmax = 40X + 50Y`
- **Solveur :** Pyomo + GLPK

### Sujet 2 — Distribution / Routage des camions d'eau
- **Responsable :** Fatimetou Mohamed Lemin Saleh (C25248)
- **Données :** `distribution_eau_data.csv`
- **Modèle :** `Zmax = 30X + 40Y`
- **Solveur :** OR-Tools Linear Solver (GLOP)

### Sujet 3 — Problème du voyageur de commerce (TSP)
- **Responsable :** Maryem Yahya Hourme (C29782)
- **Données :** `tsp_data.csv`
- **Modèle :** `Zmax = 25X + 20Y`
- **Solveur :** OR-Tools Linear Solver (GLOP)

## Résultats finaux

| Sujet | Solution optimale | Zmax |
|---|---|---|
| 1 — Transport de poissons | X = 60, Y = 40 | **4400** |
| 2 — Distribution d'eau | (X=40, Y=0) ou (X=0, Y=30) | **1200** |
| 3 — TSP (version linéaire) | X = 20, Y = 10 | **700** |

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Comment exécuter les fichiers Python

```bash
python exercices/01_transport_poissons/model_pyomo.py
python exercices/02_routage_camions_eau/model_ortools.py
python exercices/03_TSP/model_ortools.py
```

## Comment compiler les fichiers LaTeX

Pour le rapport :
```bash
cd rapport
pdflatex main.tex
pdflatex main.tex      # 2e passe pour la table des matières
```

Pour chaque exercice simplexe :
```bash
cd exercices/01_transport_poissons
pdflatex simplexe.tex
```
(idem pour `02_routage_camions_eau` et `03_TSP`)

## Présentation

La présentation orale finale (`presentation_RO.pptx`) sera ajoutée dans le dossier `presentation/` une fois terminée.
