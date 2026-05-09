from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def create_data_model():
    data = {}

    data["distance_matrix"] = [
        [0, 10, 15, 20, 25],
        [10, 0, 8, 12, 18],
        [15, 8, 0, 10, 14],
        [20, 12, 10, 0, 9],
        [25, 18, 14, 9, 0],
    ]

    data["demands"] = [0, 30, 40, 20, 50]
    data["vehicle_capacities"] = [100, 100]
    data["num_vehicles"] = 2
    data["depot"] = 0

    return data


def print_solution(data, manager, routing, solution):
    print("=== Résultat : Routage des camions d'eau ===")
    total_distance = 0
    total_load = 0

    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route_load = 0
        route = f"Camion {vehicle_id + 1}: "

        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data["demands"][node_index]
            route += f"{node_index} -> "
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)

        route += "0"
        print(route)
        print("Charge transportée :", route_load)
        print("Distance parcourue :", route_distance)
        print()

        total_distance += route_distance
        total_load += route_load

    print("Distance totale :", total_distance)
    print("Charge totale :", total_load)


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

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)

    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,
        data["vehicle_capacities"],
        True,
        "Capacity"
    )

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()