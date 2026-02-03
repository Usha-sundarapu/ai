from collections import deque

def bfs_with_steps(graph, source):
    q = deque([source])
    visited = set([source])
    parent = {source: None}
    step = 0

    while q:
        node = q.popleft()
        step += 1

        adjacent = graph.get(node, [])
        unvisited_adj = [v for v in adjacent if v not in visited]

        print(f"Step {step}")
        print(f"Source Node   : {node}")
        print(f"Adjacent Nodes: {adjacent}")
        print(f"Visited       : {sorted(visited)}")
        print(f"Unvisited Adj : {unvisited_adj}")

        for nei in unvisited_adj:
            visited.add(nei)
            parent[nei] = node
            q.append(nei)

        path = []
        cur = node
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        print(f"Path to Node  : {path[::-1]}")
        print("-" * 40)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_with_steps(graph, 'A')
