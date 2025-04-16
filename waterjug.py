from collections import deque

def water_jug_bfs():
    """Solve the Water Jug Problem using BFS."""
    capacity_4 = 4  # Capacity of 4-liter jug
    capacity_3 = 3  # Capacity of 3-liter jug
    goal = (2, 0)   # We need 2 liters in the 4-liter jug

    visited = set()  # To avoid cycles
    queue = deque([((0, 0), [])])  # (state, path)

    while queue:
        (jug4, jug3), path = queue.popleft()

        if (jug4, jug3) == goal:
            print(f"Solution found in {len(path)} steps:")
            for step in path:
                print(step)
            return path

        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))

        # Possible actions
        actions = [
            ("Fill 4L Jug", (capacity_4, jug3)),  # Fill 4L jug
            ("Fill 3L Jug", (jug4, capacity_3)),  # Fill 3L jug
            ("Empty 4L Jug", (0, jug3)),          # Empty 4L jug
            ("Empty 3L Jug", (jug4, 0)),          # Empty 3L jug
            ("Pour 4L -> 3L", (jug4 - min(jug4, capacity_3 - jug3), jug3 + min(jug4, capacity_3 - jug3))),  # Pour from 4L to 3L
            ("Pour 3L -> 4L", (jug4 + min(jug3, capacity_4 - jug4), jug3 - min(jug3, capacity_4 - jug4)))   # Pour from 3L to 4L
        ]

        for action, new_state in actions:
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    print("No solution found.")
    return None

# Run BFS to solve the problem
water_jug_bfs()
