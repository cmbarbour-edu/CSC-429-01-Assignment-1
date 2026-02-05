from collections import defaultdict
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.open = True # To indicate if the node is able to be traversed

    def set_closed(self):
        self.open = False

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_node(self, u):
        self.graph[u] = []

    def dfs(self, start_node, end_node):
        visited = list()
        parent = {}
        stack = list()
        stack.append(start_node)
        while stack:
            current = stack.pop()
            visited.append(current) # Mark node as visited
            print("Visited node ", current.value)
            if current == end_node:
                return self.backtrack_path(parent, start_node, end_node)
            else:
                for neighbor in current.neighbors:
                    if neighbor not in visited and neighbor.open:
                        stack.append(neighbor)
                        parent[neighbor] = current

    
    def bfs(self, start_node, end_node):
        queue = deque()
        visited = list()
        parent = {}
        queue.append(start_node)
        while queue:
            node = queue.popleft()
            visited.append(node) # Mark node as visited
            print("Visited node ", node.value)
            if node == end_node:
                return self.backtrack_path(parent, start_node, end_node)
            else:
                for neighbor in node.neighbors:
                    if neighbor.open and neighbor not in visited: # Only traverse if the node is open and not visited yet
                        queue.append(neighbor)
                        parent[neighbor] = node

    def backtrack_path(self, parent, start, end_node):
        path = [end_node]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path


# Create graph and nodes    
graph = Graph()
nodes = {}
for row in range(1, 8):
    for col in range(1, 7):
        nodes[(row, col)] = Node((row, col))
        graph.add_node(nodes[(row, col)])
for row in range(1, 8):
    for col in range(1, 7):
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row = row + d[0]
            neighbor_col = col + d[1]
            if 1 <= neighbor_row <= 7 and 1 <= neighbor_col <= 6:
                neighbor_node = nodes[(neighbor_row, neighbor_col)]
                nodes[(row, col)].add_neighbor(neighbor_node)
# Set nodes as closed
for closed_node in [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (3, 2), (3, 3), (3, 5),
                    (3, 6), (4, 2), (4, 3), (4, 5), (4, 6), (5, 2), (5, 5), (5, 6),
                    (6, 2), (6, 4), (6, 5), (6, 6), (1, 2), (7, 4), (7, 5), (7, 6) ]:
    for node in nodes.values():
        if node.value == closed_node:
            node.set_closed()
# Establish start and end nodes
start_node = nodes[(7, 1)]
end_node = nodes[(4, 4)]
# Do DFS and BFS
print("Performing DFS:")
result_dfs = graph.dfs(start_node, end_node)
path = ""
print("DFS Path:")
for each in result_dfs:
    if each != result_dfs[-1]:
        path += str(each.value) + " -> "
    else:
        path += str(each.value)
print(path + "\n")
print("Performing BFS:")
result_bfs = graph.bfs(start_node, end_node)
path = ""
print("BFS Path:")
for each in result_bfs:
    if each != result_bfs[-1]:
        path += str(each.value) + " -> "
    else:
        path += str(each.value)
print(path)
