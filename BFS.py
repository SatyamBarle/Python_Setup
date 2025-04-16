from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    parent = {start: None}  # To track the path
    
    while queue:
        node = queue.popleft()
        
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Return reversed path from start to goal
        
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = node
    
    return None  # Goal not found

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Test the BFS function
start_node = 'A'
goal_node = 'G'
path = bfs(graph, start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
