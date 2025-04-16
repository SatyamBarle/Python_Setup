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
# Take user input for graph structure
graph = {}
num_edges = int(input("Enter number of edges: "))

for _ in range(num_edges):
    u, v = input("Enter edge (node1 node2): ").split()
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

# Take user input for start and goal nodes
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

# Run BFS
dfs_recursive(graph, start_node, goal_node)

"""Enter number of edges: 6
Enter edge (node1 node2): A B
Enter edge (node1 node2): A C
Enter edge (node1 node2): B D
Enter edge (node1 node2): B E
Enter edge (node1 node2): C F
Enter edge (node1 node2): C G
Enter start node: A
Enter goal node: G """

