from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, maximize, SolverFactory, value


def main():
    model = ConcreteModel()

    # Variables de décision
    model.X = Var(domain=NonNegativeReals)
    model.Y = Var(domain=NonNegativeReals)

    # Fonction objectif
    model.Z = Objective(
        expr=40 * model.X + 50 * model.Y,
        sense=maximize
    )

    # Contraintes
    model.c1 = Constraint(expr=model.X + model.Y <= 100)
    model.c2 = Constraint(expr=2 * model.X + 3 * model.Y <= 240)
    model.c3 = Constraint(expr=model.X + 2 * model.Y <= 160)

    # Solveur
    solver = SolverFactory("glpk")
    result = solver.solve(model)

    print("=== Résultat : Transport de poissons ===")
    print("Status :", result.solver.status)
    print("Termination condition :", result.solver.termination_condition)
    print("X =", value(model.X))
    print("Y =", value(model.Y))
    print("Z =", value(model.Z))


if __name__ == "__main__":
    main()