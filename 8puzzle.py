import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0, h=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost (Manhattan distance)
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(board, goal):
    """Calculate the Manhattan Distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:  # Ignore empty tile
                x, y = divmod(goal.index(board[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state, goal):
    """Generate all possible moves from the current state."""
    moves = []
    x, y = [(r, c) for r in range(3) for c in range(3) if state.board[r][c] == 0][0]
    directions = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

    for move, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in state.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            moves.append(PuzzleState(new_board, state, move, state.g + 1, manhattan_distance(new_board, goal)))

    return moves

def a_star_search(start, goal):
    """A* search algorithm to solve the 8-puzzle."""
    goal_flat = sum(goal, [])  # Flatten the goal board
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, PuzzleState(start, None, "", 0, manhattan_distance(start, goal_flat)))

    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal:
            path = []
            while current.parent:
                path.append(current.move)
                current = current.parent
            return path[::-1]  # Return the path in the correct order

        closed_set.add(tuple(map(tuple, current.board)))

        for neighbor in get_neighbors(current, goal_flat):
            if tuple(map(tuple, neighbor.board)) not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None  # No solution found

# Example: Start and Goal State
start_state = [[1, 2, 3], [8, 5, 6], [4, 7, 0]]  # 0 represents the empty tile
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution = a_star_search(start_state, goal_state)

if solution:
    print(f"Solution found in {len(solution)} moves: {' -> '.join(solution)}")
else:
    print("No solution found.")
