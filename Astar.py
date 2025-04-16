import heapq

class Node:
    def __init__(self, name, cost, heuristic):
        self.name = name
        self.cost = cost        # g(n)
        self.heuristic = heuristic  # h(n)
        self.total_cost = cost + heuristic  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def a_star_or_graph(graph, start, goal, heuristics):
    open_list = []
    heapq.heappush(open_list, Node(start, 0, heuristics[start]))
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        print(f"Visiting Node: {current_node.name}, f(n): {current_node.total_cost}")

        if current_node.name == goal:
            print(f"Goal Node '{goal}' found with total cost: {current_node.total_cost}")
            return

        closed_list.add(current_node.name)

        for neighbor, cost in graph.get(current_node.name, []):
            if neighbor not in closed_list:
                g = current_node.cost + cost
                h = heuristics[neighbor]
                heapq.heappush(open_list, Node(neighbor, g, h))

    print("Goal Node not found in the graph.")

# Example OR Graph representation (adjacency list)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristics for each node
heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}

# Run A* Search on OR Graph
a_star_or_graph(graph, start='A', goal='G', heuristics=heuristics)
