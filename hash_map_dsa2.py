from collections import deque

# Problem: Find the shortest path in an unweighted graph using BFS and hash maps.
# We'll use a hash map (dictionary) to store the adjacency list of the graph.


def bfs_shortest_path(graph, start, end):
    """
    Finds the shortest path between start and end nodes in an unweighted graph using BFS.
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :param end: target node
    :return: list, shortest path from start to end (inclusive), or [] if no path exists
    """
    queue = deque()
    queue.append((start, [start]))  # Each element is (current_node, path_so_far)
    visited = set()  # To avoid revisiting nodes

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path  # Found the shortest path
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)  # Mark as visited when enqueued to avoid duplicates
    return []  # No path found

# Example 1: Simple graph
# Graph structure:
# A -- B -- C
#  \       /
#    -- D
graph1 = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print("Example 1: Shortest path from A to C")
print(bfs_shortest_path(graph1, 'A', 'C'))  # Output: ['A', 'B', 'C']

# Edge Case 1: Start and end are the same
print("\nEdge Case 1: Start and end are the same")
print(bfs_shortest_path(graph1, 'A', 'A'))  # Output: ['A']

# Edge Case 2: No path exists
graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C']
}
print("\nEdge Case 2: No path exists between A and D")
print(bfs_shortest_path(graph2, 'A', 'D'))  # Output: []

# Edge Case 3: Empty graph
graph3 = {}
print("\nEdge Case 3: Empty graph")
print(bfs_shortest_path(graph3, 'A', 'B'))  # Output: []