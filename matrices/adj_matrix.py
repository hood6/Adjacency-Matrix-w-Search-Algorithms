import numpy as np


class AdjMatrix:
    def __init__(self, size):
        if size < 1:
            print("Size of matrix must be greater than zero.")
            return
        if not isinstance(int(size), int):
            print("Size of matrix must be an integer.")
            return
        self.matrix = np.zeros((size, size), dtype=np.int32)
        self.vertex_num = 0
        self.size = size
        self.vertices = {}

    def add_vertex(self):
        if self.vertex_num == self.size:
            return
        self.vertices[self.vertex_num] = Vertex(self.vertex_num, True)
        self.vertex_num += 1

    def add_edge(self, from_vertex, to_vertex, weight=1):
        self.matrix[from_vertex][to_vertex] = weight

    def print_graph(self):
        return


class Vertex:
    def __init__(self, v_id, path):
        if not isinstance(v_id, int):
            print("Given ID is not an integer.")
            return
        else:
            self.id = v_id
        if not isinstance(path, bool):
            print("Given path is not a boolean.")
            return
        else:
            self.path = path
