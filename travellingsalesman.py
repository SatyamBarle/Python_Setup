import math

def tsp_nearest_neighbor(graph, start):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0
    current_city = start
    visited[current_city] = True

    for _ in range(n - 1):
        nearest_city = None
        min_cost = math.inf

        for city in range(n):
            if not visited[city] and 0 < graph[current_city][city] < min_cost:
                min_cost = graph[current_city][city]
                nearest_city = city

        if nearest_city is None:
            break

        path.append(nearest_city)
        visited[nearest_city] = True
        total_cost += min_cost
        current_city = nearest_city

    # Return to starting city
    total_cost += graph[current_city][start]
    path.append(start)

    print(f"\nPath: {' -> '.join(map(str, path))}")
    print(f"Total cost: {total_cost}")

# Example graph as adjacency matrix (0 means no path to itself)
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Run TSP Nearest Neighbor starting from city 0
tsp_nearest_neighbor(graph, start=0)
