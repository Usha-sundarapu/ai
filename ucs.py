import heapq
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    visited = set()
    step = 1

    print("===== UCS STEP-WISE EXECUTION =====\n")

    while priority_queue:
        print(f"Step {step}: Priority Queue ->", priority_queue)

        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(f"Expanding Node: {node} | Cost so far: {cost} | Path: {path}\n")

        visited.add(node)

        if node == goal:
            print("===== GOAL FOUND =====")
            return cost, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))

        step += 1

    return float("inf"), []

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [('G', 6)],
    'F': [('G', 1)],
    'G': []
}

start_node = 'A'
goal_node = 'G'

cost, path = uniform_cost_search(graph, start_node, goal_node)

print("\n===== FINAL RESULT =====")
print("Optimal Cost:", cost)
print("Optimal Path:", path)

G = nx.DiGraph()
for node in graph:
    for neighbor, weight in graph[node]:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)

plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_size=2000)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("UCS Optimal Solution Path")
plt.show()
