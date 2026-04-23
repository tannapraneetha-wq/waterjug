from collections import deque

# Jug capacities
CAP_A = 4
CAP_B = 3

# Goal: 2 liters in Jug A
GOAL = 2

def get_next_states(x, y):
    states = []

    # Fill Jug A
    states.append((CAP_A, y))

    # Fill Jug B
    states.append((x, CAP_B))

    # Empty Jug A
    states.append((0, y))

    # Empty Jug B
    states.append((x, 0))

    # Pour A → B
    pour = min(x, CAP_B - y)
    states.append((x - pour, y + pour))

    # Pour B → A
    pour = min(y, CAP_A - x)
    states.append((x + pour, y - pour))

    return states


def bfs():
    visited = set()
    queue = deque()

    # Store (state, path)
    queue.append(((0, 0), []))

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if x == GOAL:
            return path + [(x, y)]

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for next_state in get_next_states(x, y):
            if next_state not in visited:
                queue.append((next_state, path + [(x, y)]))

    return None


def print_solution(path):
    print("\nSolution Steps:\n")
    for i, state in enumerate(path):
        print(f"Step {i}: Jug A = {state[0]}L, Jug B = {state[1]}L")


if __name__ == "__main__":
    solution = bfs()

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")