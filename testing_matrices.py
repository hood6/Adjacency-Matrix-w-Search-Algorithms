from matrices.adj_matrix import AdjMatrix
from math import sqrt

arr_size = 9
arr_length = int(sqrt(arr_size))
arr_west_edge = arr_length-1
mat = AdjMatrix(arr_size)
for i in range(arr_size):
    mat.add_vertex()
for i in range(arr_size):
    north_id = i-arr_length
    south_id = i+arr_length
    east_id = i+1
    west_id = i-1
    if north_id >= 0:
        mat.add_edge(from_vertex=i, to_vertex=north_id)
        mat.add_edge(from_vertex=north_id, to_vertex=i)
    if south_id < arr_length:
        mat.add_edge(from_vertex=i, to_vertex=south_id)
        mat.add_edge(from_vertex=south_id, to_vertex=i)
    if east_id % arr_length != 0 and east_id < arr_size:
        mat.add_edge(from_vertex=i, to_vertex=east_id)
        mat.add_edge(from_vertex=east_id, to_vertex=i)
    if west_id % arr_length != arr_west_edge and west_id >= 0:
        mat.add_edge(from_vertex=i, to_vertex=west_id)
        mat.add_edge(from_vertex=west_id, to_vertex=i)
mat.print_dfs()
