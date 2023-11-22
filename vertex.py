""" class Vertex
        Attributes:
            row: position of row
            column: position of colomn
            color: color/status of the vertex, default to white
            width: width of the vertex, also is the weight of edges
            neighbors: list of non-wall neighbors of the vertex

        Methods:
            get_position: return the position, represented by (row, column)
            is_open, is_closed, is_barrier, is_start, is_end, is_path: return True if the vertex is of the status
            make_open, make_closed, make_barrier, make_start, make_end, make_path: change the status
            reset_grid: change vertex to the default status
            draw: draw the vertex on the grid
                Parameters: current window
            add_neighbor: add 4 adjacent vertices as neighbors if they are not walls
                Parameters: grid
"""
import pygame
from graph import Graph

WIDTH = 1000
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Odyssey")


# Colors as status of vertices
WHITE = (255, 255, 255) # default
BLACK = (0, 0, 0) # wall
RED = (255, 0, 0) # visited
GREEN = (0, 255, 0) # open
YELLOW = (255, 255, 0) # path
ORANGE = (255, 165 ,0) # start
BLUE = (0, 255, 0) # end


class Vertex:
    def __init__(self, row, column, width, total_rows, color=WHITE):
        self.row = row
        self.column = column
        self.color = color
        self.width = width
        self.total_rows = total_rows
        self.neighbors = []
        self.prev_nbr = None
    
    def is_wall(self):
        return self.color == BLACK
    
    def is_open(self):
        return self.color == GREEN
    
    def is_visited(self):
        return self.color == RED
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == BLUE
    
    def is_path(self):
        return self.color == YELLOW
    
    # def is_prev_nbr(self, vertex):
    #     return vertex == self.prev_nbr

    def set_start(self):
        self.color = ORANGE

    def set_end(self):
        self.color = BLUE

    def set_open(self):
        self.color = GREEN
    
    def set_visted(self):
        self.color = RED

    def set_wall(self):
        self.color = BLACK

    def set_path(self):
        self.color = YELLOW

    # def set_prev_nbr(self, vertex):
    #     self.prev_nbr = vertex

    def reset_vertex(self):
        self.color = WHITE

    def draw_vertex(self, window):
        # pygame draw rectangle/vertex at position (x, y) of width and height
        x = self.row * self.width
        y = self.column * self.width
        pygame.draw.rect(window, self.color, (x, y, self.width, self.width))

    # need to set the grid first, only add if it's not wall
    def add_neighbor(self, graph):
        self.neighbors = []
        row = self.row
        column = self.column
        total = self.total_rows
        # add vertex below the current vertex
        if row < total - 1 and not graph[row + 1][column].is_wall():
            self.neighbors.append(graph[row + 1][column])
        # add vertex on top of the current vertex
        if self.row > 0 and not graph[row - 1][column].is_wall():
            self.neighbors.append(graph[row - 1][column])
        # add vertex on the left
        if column > 0 and not graph[row][column - 1].is_wall():
            self.neighbors.append(graph[row][column - 1])
        # add vertex on the right
        if column < total - 1 and not graph[row][column + 1].is_wall():
            self.neighbors.append(graph[row][column + 1])

    # def get_position(self):
    #     return (self.row, self.column)
    
    def get_neighbors(self):
        return [nbr for nbr in self.neighbors]
    
    # def __str__(self):
    #     return str(self.id) + 'connects to: ' + str([nbr for nbr in self.neighbors])
    
    # def __lt__(self, other_vert):
    #     return False


# Create vertices to fill in the grid, in form of 2D List [[][][]...]
def set_grid(total_rows, width):
    grid = []
    sub_width = width // total_rows
    for row in range(total_rows):
        grid.append([])
        for col in range(total_rows):
            grid[row].append(Vertex(row, col, sub_width, total_rows))
    return grid

# TODO
# total rows不是vertex的attribute，应该写在graph里
# set grid不是vertex的功能，应该写在graph里
# 整理一下attribute和功能，分开写
# vertex：自己的行、列、状态、nbr，功能：判断&调整状态，增加nbr，记录前一个nbr
# graph：一共多少行、列，有哪些vertex，功能：画出整个graph