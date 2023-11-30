""" 
Vertex class
Attributes:
    row: index of row
    column: index of column
    color: color/status of the vertex, default to white
    width: width of the vertex; also is the weight of edges
    walls: walls in direction top, bottom, left, right, True means wall, False means not wall
    visited: for Dijkstra, to track if the vertex is visited
    neighbors: list of neighbors of the vertex; only add to the list when there's no wall between
Methods:
    getters: for Dijkstra, return True if the vertex is of the status
    setters: for Dijkstra, change the status of the vertex
    reset_vertex: in case need to change the vertex to the default status
    reset_wall: for the maze to break walls
    add_neighbors: for Dijkstra and maze, add 4 adjacent vertices as neighbors if there are no wall between
        Parameters: need to draw_graph() to get the vert_list to pass in as parameter
    get_neighbors: return the neighbors list
Function:
    draw_graph: create a 2D List to hold vertices
        Parameters:
            rows: number of rows
            width: width of each row
"""
# Colors as the status of vertices
WHITE = (255, 255, 255) # default
RED = (67, 172, 248) # visited, sky blue
GREEN = (248, 231, 75) # open, soft yellow
YELLOW = (85, 255, 0) # path, bright green
ORANGE = (255, 132, 124) # start, pink
BLUE = (183, 224, 168) # end, light green
BLACK = (0, 0, 0) # wall


class Vertex:
    def __init__(self, row, column, width, color=WHITE):
        self.row = row
        self.column = column
        self.color = color
        self.width = width
        self.walls = {'top': True, 'bottom': True, 'left': True, 'right': True}
        self.visited = False # for maze generation, flag True after being visited, to avoid using Set
        self.neighbors = []
    
    def __str__(self) -> str:
        return f"{self.row}, {self.column}"
        
    def is_wall(self, position):
        return self.walls[position]
    
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

    def set_start(self):
        self.color = ORANGE

    def set_end(self):
        self.color = BLUE

    def set_open(self):
        self.color = GREEN
    
    def set_visited(self):
        self.color = RED

    def set_path(self):
        self.color = YELLOW

    def reset_vertex(self):
        self.color = WHITE

    def reset_walls(self, walls):
        self.walls = walls

    # call this after the maze has been generated to update the neighbors list
    def add_neighbors(self, vert_list):
        row = self.row
        column = self.column
        total = len(vert_list)
        vertex = vert_list[row][column]
        # add vertex below the current vertex
        if row < total - 1 and not vertex.walls['bottom']:
            self.neighbors.append(vert_list[row + 1][column])
        # add vertex on top of the current vertex
        if self.row > 0 and not vertex.walls['top']:
            self.neighbors.append(vert_list[row - 1][column])
        # add vertex on the left
        if column > 0 and not vertex.walls['left']:
            self.neighbors.append(vert_list[row][column - 1])
        # add vertex on the right
        if column < total - 1 and not vertex.walls['right']:
            self.neighbors.append(vert_list[row][column + 1])

    def get_neighbors(self):
        return [nbr for nbr in self.neighbors]
    
    def __lt__(self, other):
        """Define the behavior for the '<' operator (less than)."""
        if isinstance(other, Vertex):
            return self == other


def draw_graph(rows, width):
        graph = []
        sub_width = width // rows
        for row in range(rows):
            graph.append([])
            for column in range(rows):
                graph[row].append(Vertex(row, column, sub_width))
        return graph

def get_all_vertices(graph):
    ls = []
    for row in graph:
        for v in row:
            ls.append(v)
    return ls

# MOVED to main(), call this when maze has been generated to draw wall if there's any
# def draw_wall(self, window):
#     # pygame draw line from one position to another
#     width = self.width
#     x = self.row * width
#     y = self.column * width
#     # draw top wall
#     if self.walls['top']:
#         pygame.draw.line(window, BLACK, (x, y), (x + width, y))
#     # draw right wall
#     if self.walls['right']:
#         pygame.draw.line(window, BLACK, (x + width, y), (x + width, y + width))
#     # draw bottom wall
#     if self.walls['bottom']:
#         pygame.draw.line(window, BLACK, (x + width, y + width), (x, y + width))
#     # draw left wall
#     if self.walls['left']:
#         pygame.draw.line(window, BLACK, (x, y + width), (x, y))
