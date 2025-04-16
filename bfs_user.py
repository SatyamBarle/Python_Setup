from collections import deque

def bfs(graph, start, goal):
    """Breadth-First Search algorithm to find the goal node."""
    queue = deque([[start]])  # Queue stores paths, not just nodes
    visited = set()

    while queue:
        path = queue.popleft()  # Get and remove the first path
        node = path[-1]  # Last node in the path

        if node == goal:
            print(f"Path found: {' -> '.join(path)}")
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)  # Copy current path
                new_path.append(neighbor)
                queue.append(new_path)  # Enqueue new path

    print("No path found.")
    return None

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
bfs(graph, start_node, goal_node)

"""Enter number of edges: 6
Enter edge (node1 node2): A B
Enter edge (node1 node2): A C
Enter edge (node1 node2): B D
Enter edge (node1 node2): B E
Enter edge (node1 node2): C F
Enter edge (node1 node2): C G
Enter start node: A
Enter goal node: G """
