from matrices.adj_matrix import AdjMatrix
from collections import deque
from sys import maxsize


def min_distance(dist_list):
    min_dist = maxsize
    for i in dist_list:
        if i < min_dist:
            min_dist = i
    return dist_list.index(i)


def dijkstras(g, start_id, end_id):
    if not isinstance(g, AdjMatrix):
        print("Parameter is not a graph.")
        return None
    distance = {}
    for i in range(g.size):
        distance[i] = maxsize
    distance[start_id] = 0
    queue = []
    for key in g.vertices:
        queue.append(key)
    visited = []
    while queue:
        check = maxsize
        for i in queue:
            if distance[i] < check:
                check = distance[i]
                curr_id = i
        queue.remove(curr_id)
        visited.append(curr_id)
        for v_id in g.vertices:
            if g.matrix[curr_id][v_id] == 1:
                dist = distance[curr_id] + g.matrix[curr_id][v_id]
                if dist < distance[v_id]:
                    distance[v_id] = dist
    print(distance)

