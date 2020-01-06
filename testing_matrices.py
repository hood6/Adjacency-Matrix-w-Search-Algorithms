from matrices.adj_matrix import AdjMatrix

arr_length = 3  # Length of the square graph
arr_size = arr_length*arr_length  # Total number of nodes in the graph
arr_west_edge = arr_length-1
mat = AdjMatrix(arr_size)
for i in range(arr_size):  # Adds vertices to the graph
    mat.add_vertex()
for i in range(arr_size):  # Adds edges to the matrix
    north_id = i-arr_length  # Potential ID of the node above the current node
    south_id = i+arr_length  # Potential ID of the node below the current node
    east_id = i+1  # Potential ID of the node to the right of the current node
    west_id = i-1  # Potential ID of the node to the left of the current node
    """
    Checks the potential ID of the node above the current node to make sure
    that it is within the bounds of the graph. If the statement returns false,
    no edge is added
    """
    if north_id >= 0:
        mat.add_edge(from_vertex=i, to_vertex=north_id)
        mat.add_edge(from_vertex=north_id, to_vertex=i)
    """
    Checks the potential ID of the node below the current node to make sure
    that it is within the bounds of the graph. If the statement returns false,
    meaning that the ID is greater than the length of the graph, no edge is added.
    """
    if south_id < arr_length:
        mat.add_edge(from_vertex=i, to_vertex=south_id)
        mat.add_edge(from_vertex=south_id, to_vertex=i)
    """
    Checks the potential ID of the node to the right of the current node. This
    check ensures that a node on the right side of the graph does not connect
    to the next node on the left side and that the ID is less than the size of
    the graph. If either statement returns false, no edge is added.
    """
    if east_id % arr_length != 0 and east_id < arr_size:
        mat.add_edge(from_vertex=i, to_vertex=east_id)
        mat.add_edge(from_vertex=east_id, to_vertex=i)
    """
    Checks the potential ID of the node to the left of the current node. This
    check ensures that a node on the left side of the graph does not connect to
    the previous node on the right side and that the ID is not less than 0. If
    either statement returns false, no edge is added.
    """
    if west_id % arr_length != arr_west_edge and west_id >= 0:
        mat.add_edge(from_vertex=i, to_vertex=west_id)
        mat.add_edge(from_vertex=west_id, to_vertex=i)
mat.print_dfs() # Prints the contents of the graph using Depth first search
