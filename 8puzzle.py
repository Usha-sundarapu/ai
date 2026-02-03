import heapq

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)  # 0 = blank


def manhattan(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL_STATE.index(tile)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx * 3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))

    return neighbors


def solve_8_puzzle(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [state])
                )

    return None


def print_solution(solution):
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print("-----")


if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    solution = solve_8_puzzle(start_state)

    if solution:
        print(f"Solution found in {len(solution) - 1} moves:\n")
        print_solution(solution)
    else:
        print("No solution found.")
