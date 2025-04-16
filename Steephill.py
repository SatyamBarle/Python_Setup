def steepest_hill_climb(graph, heuristic, start, goal):
    """Steepest-Ascent Hill Climbing algorithm to find the goal node."""
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            print("No path found.")
            return None

        # Choose the neighbor with the highest heuristic value
        best_neighbor = max(neighbors, key=lambda node: heuristic[node], default=None)

        if heuristic[best_neighbor] <= heuristic[current]:  # Stop if no improvement
            print("Local maximum reached. No path found.")
            return None
        
        current = best_neighbor
        path.append(current)

    print(f"Path found: {path}")
    return path

# Define the graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': []
}

# Define heuristic values (higher is better)
heuristic = {
    'A': 1, 'B': 3, 'C': 4, 'D': 2, 'E': 5, 'F': 6, 'G': 7, 'H': 8
}

# Start node, goal node
start_node = 'A'
goal_node = 'H'

# Run the Steepest-Ascent Hill Climbing algorithm
steepest_hill_climb(graph, heuristic, start_node, goal_node)
