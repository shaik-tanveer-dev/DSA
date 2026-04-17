# Graph:
# 1)Graph is a non-linear data structure used to represent relationships.
# 2)It consists of:
#     ->Vertices(Nodes)->points(A,B,C..)
#     ->Edges->connections between Nodes
# Eg: People connected in a social networks
#     cities connected by nodes
#     web pages connected by links.
# real life example:
#   ->Google Maps network:
#             ->Locations -Nodes
#             ->Roads -Edges
# 3)Types of graphs:
#  1)unweighted Graph
#  2)Weighted Graph
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['D'],
    'D':[],
}

visited = set()
bfs(graph, 'A', visited)