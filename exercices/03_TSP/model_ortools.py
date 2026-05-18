"""
Sujet 3 : Probleme du voyageur de commerce (TSP)
=================================================
Modele de programmation lineaire (PL) resolu avec OR-Tools
Linear Solver (GLOP), pour correspondre EXACTEMENT au modele
simplexe theorique du rapport.

Variables   : X = nombre de trajets effectues sur la route 1
              Y = nombre de trajets effectues sur la route 2
Objectif    : maximiser Z = 25 X + 20 Y
Contraintes : X + Y    <= 30
              4X + 2Y  <= 100
              2X + 3Y  <= 90
              X, Y >= 0
Solveur     : OR-Tools Linear Solver (GLOP)
Resultat    : X = 20, Y = 10, Zmax = 700
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
    solver.Add(X + Y       <= 30)    # nombre maximal de trajets
    solver.Add(4 * X + 2 * Y <= 100)  # ressource A
    solver.Add(2 * X + 3 * Y <= 90)   # ressource B

    # --- Fonction objectif : max Z = 25 X + 20 Y ------------------
    solver.Maximize(25 * X + 20 * Y)

    return solver, X, Y


def print_results(solver, X, Y, status) -> None:
    """Affiche les resultats de maniere structuree."""
    print("=" * 60)
    print("  Sujet 3 : Probleme du voyageur de commerce, TSP (PL)")
    print("=" * 60)

    if status == pywraplp.Solver.OPTIMAL:
        print("  Statut : OPTIMAL")
        print("-" * 60)
        print(f"  X (trajets route 1) = {X.solution_value():.2f}")
        print(f"  Y (trajets route 2) = {Y.solution_value():.2f}")
        print(f"  Zmax (gain total)   = {solver.Objective().Value():.2f}")
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
