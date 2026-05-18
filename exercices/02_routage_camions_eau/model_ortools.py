"""
Sujet 2 : Routage des camions d'eau
====================================
Modele de programmation lineaire (PL) resolu avec OR-Tools
Linear Solver (GLOP), pour correspondre EXACTEMENT au modele
simplexe theorique du rapport.

Variables   : X = nombre de tournees vers la zone 1
              Y = nombre de tournees vers la zone 2
Objectif    : maximiser Z = 30 X + 40 Y
Contraintes : X + Y    <= 50
              3X + 4Y  <= 120
              2X + 5Y  <= 150
              X, Y >= 0
Solveur     : OR-Tools Linear Solver (GLOP)
Resultat    : Zmax = 1200
              Deux solutions optimales possibles :
                  (X = 40, Y = 0)
                  (X = 0,  Y = 30)
"""

from ortools.linear_solver import pywraplp


def build_model():
    """Construit le modele de PL avec OR-Tools."""
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if solver is None:
        raise RuntimeError("Le solveur GLOP n'est pas disponible.")

    # --- Variables de decision (X, Y >= 0) -------------------------
    X = solver.NumVar(0.0, solver.infinity(), "X")
    Y = solver.NumVar(0.0, solver.infinity(), "Y")

    # --- Contraintes -----------------------------------------------
    solver.Add(X + Y       <= 50)    # nombre de tournees
    solver.Add(3 * X + 4 * Y <= 120)  # capacite/ressource A
    solver.Add(2 * X + 5 * Y <= 150)  # capacite/ressource B

    # --- Fonction objectif : max Z = 30 X + 40 Y ------------------
    solver.Maximize(30 * X + 40 * Y)

    return solver, X, Y


def print_results(solver, X, Y, status) -> None:
    """Affiche les resultats de maniere structuree."""
    print("=" * 60)
    print("  Sujet 2 : Routage des camions d'eau (PL)")
    print("=" * 60)

    if status == pywraplp.Solver.OPTIMAL:
        print("  Statut : OPTIMAL")
        print("-" * 60)
        print(f"  X (tournees zone 1) = {X.solution_value():.2f}")
        print(f"  Y (tournees zone 2) = {Y.solution_value():.2f}")
        print(f"  Zmax (eau totale)   = {solver.Objective().Value():.2f}")
        print("-" * 60)
        print("  Note : ce modele admet plusieurs solutions optimales")
        print("         equivalentes (toutes donnent Zmax = 1200) :")
        print("           - (X = 40, Y = 0)")
        print("           - (X = 0,  Y = 30)")
        print("=" * 60)
    else:
        print(f"  Statut : NON OPTIMAL (code {status})")
        print("=" * 60)


def main() -> None:
    solver, X, Y = build_model()
    status = solver.Solve()
    print_results(solver, X, Y, status)


if __name__ == "__main__":
    main()
