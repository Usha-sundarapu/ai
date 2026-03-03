from collections import deque

initial_state = ("door", "floor", "window", False)
goal_state = ("middle", "box", "middle", True)

positions = ["door", "middle", "window"]

def is_goal(state):
    return state[3] == True

def get_next_states(state):
    monkey_pos, monkey_status, box_pos, has_banana = state
    next_states = []

    # Walk action
    if monkey_status == "floor":
        for pos in positions:
            if pos != monkey_pos:
                next_states.append((
                    (pos, "floor", box_pos, has_banana),
                    f"Walk from {monkey_pos} to {pos}"
                ))

    # Push action
    if monkey_status == "floor" and monkey_pos == box_pos:
        for pos in positions:
            if pos != monkey_pos:
                next_states.append((
                    (pos, "floor", pos, has_banana),
                    f"Push box from {monkey_pos} to {pos}"
                ))

    # Climb action
    if monkey_status == "floor" and monkey_pos == box_pos:
        next_states.append((
            (monkey_pos, "box", box_pos, has_banana),
            "Climb onto box"
        ))

    # Grab action
    if monkey_pos == "middle" and monkey_status == "box" and not has_banana:
        next_states.append((
            (monkey_pos, "box", box_pos, True),
            "Grab banana"
        ))

    return next_states

def bfs():
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if is_goal(state):
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state, action in get_next_states(state):
            queue.append((next_state, path + [action]))

    return None

solution = bfs()

if solution:
    print("Solution found:\n")
    for step in solution:
        print(step)
else:
    print("No solution found.")
