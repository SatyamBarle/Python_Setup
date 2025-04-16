def dfs_recursive(graph, node, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)

    if node == goal:
        print(f"Goal node {goal} found! Path: {' -> '.join(path)}")
        return True

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, goal, visited, path):
                return True  # Stop when the goal is found

    path.pop()  # Backtrack if goal not found
    return False

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Start DFS from 'A' to find 'H'
dfs_recursive(graph, 'A', 'H')
