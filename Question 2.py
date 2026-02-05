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

    def dls(self, start_node, end_node, depth_limit):
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
            if (abs(start_node.value[0] - current.value[0]) + abs(start_node.value[1] - current.value[1]) < depth_limit):
                for neighbor in current.neighbors:
                    if neighbor not in visited and neighbor.open:
                        stack.append(neighbor)
                        parent[neighbor] = current
            else:
                print("Depth limit reached at node ", current.value)

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
print("Performing DLS with depth limit 4:")
result_dls = graph.dls(start_node, end_node, 4)
path = ""
print("DLS Path:")
if result_dls != None:    
    for each in result_dls:
        if each != result_dls[-1]:
            path += str(each.value) + " -> "
        else:
            path += str(each.value)
    print(path + "\n")
else:
    print("No path found within depth limit.\n")
print("Performing DLS with depth limit 8:")
result_dls = graph.dls(start_node, end_node, 8)
path = ""
print("DLS Path:")
if result_dls != None:    
    for each in result_dls:
        if each != result_dls[-1]:
            path += str(each.value) + " -> "
        else:
            path += str(each.value)
    print(path)
else:
    print("No path found within depth limit.")