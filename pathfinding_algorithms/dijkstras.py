from matrices.adj_matrix import AdjMatrix
from collections import deque
from sys import maxsize


def dijkstras(g, end_id):
    if not isinstance(g, AdjMatrix):
        print("Parameter is not a graph.")
        return None
    distance = [maxsize] * g.size
    distance[g.origin_id] = 0
    queue = deque([])
    for key in g.vertices:
        queue.append(key)
    visited = []
    print(queue)
    print(visited)
    while queue:
        visited.append(queue.popleft())
    print(queue)
    print(visited)

