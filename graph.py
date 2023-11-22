""" DRAFT: need to revise!!!
    class Graph
        Attributes:
            rows: total rows and columns in the graph
            vert_list: list of all vertices in the graph
            vert_count: number of vertices in the graph

        Methods:
            draw_graph: create vertices to fill in the graph, MAZE ALGO USE THIS
                Parameters:
                    rows: number of rows and columns in total in the graph
                    width: width of the grid
"""
from vertex import Vertex


class Graph:
    def __init__(self, rows):
        self.rows = rows
        self.vert_list = []
        self.vert_count = 0

    def draw_graph(self, rows, width):
        graph = self.vert_list
        sub_width = width // rows
        for row in range(rows):
            graph.append([])
            for column in range(rows):
                graph[row].append(Vertex(row, column, sub_width))
                self.vert_count += 1
        return graph
    
    
    # def add_vertex(self, key):
    #     self.vert_count = self.numVertices + 1
    #     vertex = Vertex(key)
    #     self.vert_list[key] = vertex
    #     return vertex

    def get_vertex(self, vertex):
        if vertex in self.vert_list:
            return self.vert_list[vertex]
        else:
            return None

    # def __contains__(self, vertex):
    #     return vertex in self.vert_list

    # def add_edge(self, f, t, weight=0):
    #     if f not in self.vert_list:
    #         nv = self.add_vertex(f)
    #     if t not in self.vert_list:
    #         nv = self.add_vertex(t)
    #     self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    # def get_vertices(self):
    #     return self.vert_list.keys()

    # def __iter__(self):
    #     return iter(self.vert_list.values())