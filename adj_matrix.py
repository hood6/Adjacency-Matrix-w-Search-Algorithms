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
        self.origin_id = 0
        self.size = size
        self.vertices = {}
        self.marked_list = []
        self.prev_v = 0

    def ret_vertex(self, v_id):
        if 0 <= v_id < self.size:
            print(f"Vertex ID must be [0, {self.size})")
            return
        return self.vertices[v_id]

    def add_vertex(self):
        if self.vertex_num == self.size:
            return
        self.vertices[self.vertex_num] = Vertex(self.vertex_num, True)
        self.vertex_num += 1

    def add_edge(self, from_vertex, to_vertex, weight=1):
        self.matrix[from_vertex][to_vertex] = weight

    def print_dfs(self):
        self.marked_list.clear()
        self.print_dfs_re(self.origin_id)

    def print_dfs_re(self, v_id):
        print(self.vertices[v_id].to_string())
        for i in range(len(self.vertices)):
            if i not in self.marked_list and self.matrix[v_id][i] != 0:
                self.marked_list.append(v_id)
                self.print_dfs_re(i)


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

    def to_string(self):
        return f"ID: {self.id} --- Pathable: {self.path}"
