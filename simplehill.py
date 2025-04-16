import random

def hill_climb(graph, heuristic, start, goal):
    """Simple Hill Climbing algorithm to find the goal node."""
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            print("No path found.")
            return None

        # Select the neighbor with the best heuristic value
        next_node = max(neighbors, key=lambda node: heuristic[node], default=None)

        if heuristic[next_node] <= heuristic[current]:  # Stop if no improvement
            print("Local maximum reached. No path found.")
            return None
        
        current = next_node
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

# Run the Hill Climbing algorithm
hill_climb(graph, heuristic, start_node, goal_node)
