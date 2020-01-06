import numpy as np


class AdjMatrix:
    def __init__(self, size):
        """ Initializes adjacency matrix

        Creates a 2D array that represents the edges between the vertices
        of the graph, as well as a dictionary of all vertices in the
        graph, the number of vertices. For the print function, the origin
        and marked vertices list is also initialized.

        @param size: The number of vertices that will be initialized in the
        graph
        """
        # TODO Remove some redundant variables
        if size < 1:
            print("Size of matrix must be greater than zero.")
            return
        if not isinstance(int(size), int):
            print("Size of matrix must be an integer.")
            return
        self.matrix = np.zeros((size, size), dtype=np.int32)
        self.vertex_num = 0
        self.origin_id = 1
        self.size = size
        self.vertices = {}
        self.marked_list = []
        self.to_visit = []
        self.prev_v = 0

    def ret_vertex(self, v_id):
        """ Returns the vertex of the ID passed in

        @param v_id: ID of the vertex being searched for
        @return: Vertex with the ID that was passed in
        """
        if 0 <= v_id < self.size:
            print(f"Vertex ID must be [0, {self.size})")
            return
        return self.vertices[v_id]

    def add_vertex(self):
        """ Adds a vertex to the graph

        Checks to make sure that the vertex being added will
        not exceed the size of the graph. If it is not, then it
        is added to the dictionary with the key being the ID of
        the vertex being added. The vertex_num variable is increased
        by 1. Each vertex created is by default pathable.

        """
        if self.vertex_num == self.size:
            return
        self.vertices[self.vertex_num] = Vertex(self.vertex_num, True)
        self.vertex_num += 1

    def add_edge(self, from_vertex, to_vertex, weight=1):
        """ Adds an edge to the matrix

        Adds a weight to the matrix to represent an edge between
        two vertices. By default, the weight is 1 if no weight is
        passed in. This is compatible with undirectional and
        directional graphs.

        @param from_vertex: The vertex that the edge comes from
        @param to_vertex: The vertex that the edge goes to
        @param weight: The value of the edge, represented by an
        integer
        """
        # TODO Makes weights compatible with float values ranging from 0 to 1
        self.matrix[from_vertex][to_vertex] = weight

    def print_dfs(self):
        """ Uses the Depth First Search algorithm to print the graph

        This function is called to print the graph using a depth first
        search algorithm. After ensuring that the marked vertex list is
        cleared, this function calls on the print_dfs_re utility function
        to perform most of the work and passes the origin of the graph to
        it.

        """
        self.marked_list.clear()
        for key in self.vertices:
            self.to_visit.append(key)
        self.print_dfs_re(self.origin_id)

    def print_dfs_re(self, v_id):
        """ Called on by the print_dfs function to print the graph

        This utility function makes use of depth first search to print
        the graph to the console. Initially the function checks the
        edges on the matrix of the ID passed in. If it comes upon an edge
        that does not lead to a marked vertex, the current ID is appended
        to the list, and the ID that the edge leads to is passed into the
        function recursively.

        @param v_id: The vertex ID that represents the 'from' vertex
        """
        # TODO Last node printed twice when origin is changed.
        print(self.vertices[v_id].to_string())
        for i in range(len(self.vertices)):
            if i not in self.marked_list and i in self.to_visit and self.matrix[v_id][i] != 0:
                self.marked_list.append(v_id)
                if i in self.to_visit:
                    self.to_visit.remove(i)
                self.print_dfs_re(i)


class Vertex:
    """ Framework for the vertices in the graph

    The Vertex objects hold a unique ID number as well
    as a boolean value that indicates whether the node is
    pathable or not.

    """
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


"""
Notes:
    - For pathfinding algorithms, I could also just have vertices
        with no edges to represent obstacles rather than a
        boolean that determines whether or not the vertex is pathable
        or not.
"""
