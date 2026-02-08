from collections import defaultdict
from collections import deque
from memory_profiler import memory_usage
from multiprocessing import freeze_support

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

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
                    if neighbor not in visited:
                        stack.append(neighbor)
                        parent[neighbor] = current

    def bfs(self, start_node, end_node):
        queue = deque()
        visited = list()
        parent = {}
        queue.append(start_node)
        while queue:
            current = queue.popleft()
            visited.append(current) # Mark node as visited
            print("Visited node ", current.value)
            if current == end_node:
                return self.backtrack_path(parent, start_node, end_node)
            else:
                for neighbor in current.neighbors:
                    if neighbor not in visited: # Only traverse if the node is not visited yet
                        queue.append(neighbor)
                        parent[neighbor] = current

    def backtrack_path(self, parent, start, end_node):
        path = [end_node]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path



# Create graph and nodes    
graph = Graph()
nodes = {c: Node(c) for c in "ABCDEF"}

for u, v in [('A','B'), ('B','C'), ('B','D'), ('C','E'), ('D','F')]:
	nodes[u].add_neighbor(nodes[v])

for node in nodes.values():
	graph.add_node(node)
start_node, end_node = nodes['A'], nodes['E']

if __name__ == '__main__':
    freeze_support()

    # Define memory profiling wrapper
    def bfs_wrapper():
        graph.bfs(start_node, end_node)
        print("BFS complete\n")

    def dfs_wrapper():
        graph.dfs(start_node, end_node)
        print("DFS complete\n")

    # Measure memory usage
    bfs_memory = memory_usage(bfs_wrapper, max_usage=True)
    dfs_memory = memory_usage(dfs_wrapper, max_usage=True)
    print("Memory used by BFS: " + str(bfs_memory) + " MiB")
    print("Memory used by DFS: " + str(dfs_memory) + " MiB\n")

    # Do DFS and BFS
    print("Performing DFS:")
    result_dfs = graph.dfs(start_node, end_node)
    path = ""
    print("DFS Path:")
    for each in result_dfs:
        if each != result_dfs[-1]:
            path += each.value + " -> "
        else:
            path += each.value
    print(path + '\n')
    print("Performing BFS:")
    result_bfs = graph.bfs(start_node, end_node)
    path = ""
    print("BFS Path:")
    for each in result_bfs:
        if each != result_bfs[-1]:
            path += each.value + " -> "
        else:
            path += each.value
    print(path)
