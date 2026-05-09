from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def create_data_model():
    data = {}

    data["distance_matrix"] = [
        [0, 12, 10, 19, 8],
        [12, 0, 6, 15, 11],
        [10, 6, 0, 7, 9],
        [19, 15, 7, 0, 13],
        [8, 11, 9, 13, 0],
    ]

    data["num_vehicles"] = 1
    data["depot"] = 0

    return data


def print_solution(manager, routing, solution):
    print("=== Résultat : Problème du voyageur de commerce, TSP ===")

    index = routing.Start(0)
    route = "Route optimale : "
    total_distance = 0

    while not routing.IsEnd(index):
        route += f"{manager.IndexToNode(index)} -> "
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

    route += str(manager.IndexToNode(index))

    print(route)
    print("Distance totale :", total_distance)


def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]),
        data["num_vehicles"],
        data["depot"]
    )

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(manager, routing, solution)
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()