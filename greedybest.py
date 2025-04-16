import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    """Greedy Best-First Search algorithm for finding the goal node."""
    open_list = [(heuristic[start], start)]  # Priority queue (min-heap)
    came_from = {start: None}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)  # Get the node with the lowest heuristic

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            print(f"Path found: {path}")
            return path

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current

    print("No path found.")
    return None

# Define the OR Graph (adjacency list)
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

# Define heuristic values (lower is better)
heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 1, 'F': 4, 'G': 3, 'H': 0
}

# Start node, goal node
start_node = 'A'
goal_node = 'H'

# Run the Greedy Best-First Search
greedy_best_first_search(graph, heuristic, start_node, goal_node)
