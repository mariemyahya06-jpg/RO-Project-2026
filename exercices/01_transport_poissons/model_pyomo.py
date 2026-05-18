"""
Sujet 1 : Transport de poissons Nouadhibou - Nouakchott
========================================================
Modele de programmation lineaire (PL) resolu avec Pyomo + GLPK.

Variables   : X = quantite vers le marche principal
              Y = quantite vers les restaurants/supermarches
Objectif    : maximiser Z = 40 X + 50 Y
Contraintes : capacite, transport, conservation
Solveur     : GLPK
Resultat    : X = 60, Y = 40, Z_max = 4400
"""

from pyomo.environ import (
    ConcreteModel,
    Var,
    Objective,
    Constraint,
    NonNegativeReals,
    maximize,
    SolverFactory,
    value,
)


def build_model() -> ConcreteModel:
    """Construit le modele de programmation lineaire."""
    model = ConcreteModel()

    # --- Variables de decision ---------------------------------------
    model.X = Var(domain=NonNegativeReals)
    model.Y = Var(domain=NonNegativeReals)

    # --- Fonction objectif -------------------------------------------
    # Maximiser le benefice total : Z = 40 X + 50 Y
    model.Z = Objective(
        expr=40 * model.X + 50 * model.Y,
        sense=maximize,
    )

    # --- Contraintes -------------------------------------------------
    model.c1 = Constraint(expr=model.X + model.Y <= 100)        # capacite globale
    model.c2 = Constraint(expr=2 * model.X + 3 * model.Y <= 240)  # transport
    model.c3 = Constraint(expr=model.X + 2 * model.Y <= 160)      # conservation

    return model


def print_results(model: ConcreteModel, result) -> None:
    """Affiche les resultats de maniere structuree."""
    print("=" * 60)
    print("  Sujet 1 : Transport de poissons Nouadhibou - Nouakchott")
    print("=" * 60)
    print(f"  Statut du solveur     : {result.solver.status}")
    print(f"  Condition d'arret     : {result.solver.termination_condition}")
    print("-" * 60)
    print(f"  X (marche principal)  = {value(model.X):.2f}")
    print(f"  Y (restaurants)       = {value(model.Y):.2f}")
    print(f"  Z_max (benefice)      = {value(model.Z):.2f}")
    print("=" * 60)


def main() -> None:
    model = build_model()
    solver = SolverFactory("glpk")
    result = solver.solve(model)
    print_results(model, result)


if __name__ == "__main__":
    main()
