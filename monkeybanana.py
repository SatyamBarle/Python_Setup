from collections import deque

def monkey_banana_bfs():
    """Solves the Monkey and Banana problem using BFS."""
    # Initial state: (Monkey at A, Box at B, Monkey not on box, Banana not reached)
    initial_state = ('A', 'B', False, False)
    goal_state = (None, None, None, True)  # Goal when banana is reached

    # Possible actions and their effects
    actions = {
        "Move to A": lambda s: ('A', s[1], s[2], s[3]),
        "Move to B": lambda s: ('B', s[1], s[2], s[3]),
        "Move to C": lambda s: ('C', s[1], s[2], s[3]),
        "Push Box to A": lambda s: ('A', 'A', s[2], s[3]) if s[0] == s[1] else s,
        "Push Box to B": lambda s: ('B', 'B', s[2], s[3]) if s[0] == s[1] else s,
        "Push Box to C": lambda s: ('C', 'C', s[2], s[3]) if s[0] == s[1] else s,
        "Climb on Box": lambda s: (s[0], s[1], True, s[3]) if s[0] == s[1] else s,
        "Grab Banana": lambda s: (None, None, None, True) if s[2] else s
    }

    queue = deque([(initial_state, [])])  # (State, Path)
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            print(f"Solution found in {len(path)} steps:")
            for step in path:
                print(step)
            return path

        if state in visited:
            continue
        visited.add(state)

        for action, transition in actions.items():
            new_state = transition(state)
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    print("No solution found.")
    return None

# Run the BFS to solve the problem
monkey_banana_bfs()
