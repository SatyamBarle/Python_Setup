class AOStar:
    def __init__(self, graph, heuristic, start):
        self.graph = graph                  # AO graph as adjacency list
        self.heuristic = heuristic          # Heuristic values
        self.start = start                  # Start node
        self.status = {}                    # Status of each node: -1 = solved, 0 = unsolved
        self.solution_graph = {}            # Final solution graph (optimal path)

    def get_minimum_cost_child_nodes(self, node):
        ''' Returns the child nodes and their total cost for the most promising path '''
        if node not in self.graph or len(self.graph[node]) == 0:
            return 0, []

        cost_list = []
        for child_nodes in self.graph[node]:
            cost = 0
            nodes = []
            for (child, edge_cost) in child_nodes:
                cost += self.heuristic[child] + edge_cost
                nodes.append(child)
            cost_list.append((cost, nodes))

        # Return child nodes set with minimum cost
        min_cost, min_nodes = min(cost_list, key=lambda x: x[0])
        return min_cost, min_nodes

    def ao_star(self, node):
        ''' Recursively applies the AO* algorithm '''
        print(f"Expanding Node: {node}")

        cost, child_nodes = self.get_minimum_cost_child_nodes(node)

        if len(child_nodes) == 0:
            self.status[node] = -1  # Mark as solved
            return

        # Update heuristic value
        self.heuristic[node] = cost
        self.solution_graph[node] = child_nodes

        # Recursively apply AO* to child nodes if they are not solved
        for child in child_nodes:
            if self.status.get(child, 0) != -1:
                self.ao_star(child)

        # If all child nodes are solved, mark this node as solved
        if all(self.status.get(child, 0) == -1 for child in child_nodes):
            self.status[node] = -1

    def print_solution(self):
        print("\nOptimal Solution Graph:")
        for key in self.solution_graph:
            print(f"{key} --> {self.solution_graph[key]}")

# Example AO Graph:
# Each node connects to a list of possible choices (OR)
# Each choice is a list of AND-connected child nodes with their respective edge costs
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 3)]],
    'B': [[('E', 1)], [('F', 2)]],
    'C': [[('G', 2)]],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristics for each node
heuristic = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 7,
    'E': 3,
    'F': 5,
    'G': 2
}

# Run AO* Algorithm
ao_star = AOStar(graph, heuristic, start='A')
ao_star.ao_star('A')
ao_star.print_solution()
