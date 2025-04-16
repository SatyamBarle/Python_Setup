from collections import deque

def is_valid(state):
    """Check if a state is valid (no missionaries eaten)."""
    M_left, C_left, boat, M_right, C_right = state

    # Condition to ensure missionaries are not outnumbered
    if (M_left < C_left and M_left > 0) or (M_right < C_right and M_right > 0):
        return False
    return True

def get_next_states(state):
    """Generate all possible next states."""
    M_left, C_left, boat, M_right, C_right = state
    next_states = []
    
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible boat movements

    for M, C in moves:
        if boat == 1:  # Boat on the left side
            new_state = (M_left - M, C_left - C, 0, M_right + M, C_right + C)
        else:  # Boat on the right side
            new_state = (M_left + M, C_left + C, 1, M_right - M, C_right - C)

        if min(new_state) >= 0 and is_valid(new_state):  # Check if state is valid
            next_states.append(new_state)

    return next_states

def missionaries_and_cannibals_bfs():
    """Solve the Missionaries and Cannibals problem using BFS."""
    initial_state = (3, 3, 1, 0, 0)  # (M_left, C_left, boat, M_right, C_right)
    goal_state = (0, 0, 0, 3, 3)
    
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

        for new_state in get_next_states(state):
            queue.append((new_state, path + [new_state]))

    print("No solution found.")
    return None

# Run the BFS to solve the problem
missionaries_and_cannibals_bfs()
