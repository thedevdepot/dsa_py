# hash_map_dfs.py

# Example: Depth First Search (DFS) in a graph using adjacency list (hash map)

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    if start not in graph:
        print(f"Node '{start}' not found in graph.")
        return order
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

if __name__ == "__main__":
    # Example graph as an adjacency list (hash map)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': []
    }

    print("DFS traversal starting from node 'A':")
    order = dfs(graph, 'A')
    print("Order:", order)

    # Edge case 1: Empty graph
    print("\nDFS traversal on empty graph:")
    order = dfs({}, 'A')
    print("Order:", order)

    # Edge case 2: Graph with a single node and no edges
    print("\nDFS traversal on single-node graph:")
    single_node_graph = {'X': []}
    order = dfs(single_node_graph, 'X')
    print("Order:", order)