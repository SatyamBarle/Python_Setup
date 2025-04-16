def dls(graph, node, goal, depth, path):
    """Depth-Limited Search (DLS) used in IDDFS"""
    path.append(node)

    if node == goal:
        print(f"Goal node {goal} found! Path: {' -> '.join(path)}")
        return True

    if depth == 0:
        path.pop()  # Backtrack
        return False

    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, depth - 1, path):
            return True

    path.pop()  # Backtrack
    return False

def iddfs(graph, start, goal, max_depth):
    """Iterative Deepening DFS"""
    for depth in range(max_depth):
        path = []
        if dls(graph, start, goal, depth, path):
            return True
    print("Goal node not found.")
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

# Start IDDFS from 'A' to find 'H' with max depth = 5
iddfs(graph, 'A', 'H', max_depth=5)
