""" class Vertex
        Attributes:
            row: position of row
            column: position of column
            color: color/status of the vertex, default to white
            width: width of the vertex, also is the weight of edges
            walls: walls in direction top, bottom, left, right, True means wall, False means not wall
            visited: for generating maze, to track if the vertex is visited
            neighbors: list of neighbors of the vertex, only add to the list when there's no wall between

        Methods:
            is_open, is_closed, is_barrier, is_start, is_end, is_path: for dijkstra, return True if the vertex is of the status
            
            make_open, make_closed, make_barrier, make_start, make_end, make_path: for dijkstra, change the status
            
            reset_grid: just in case need to change vertex to the default status
            
            add_neighbor: for dijkstra and maze, add 4 adjacent vertices as neighbors if there are no wall between
                Parameters: need to draw_graph() to get the vert_list to pass in as parameter
            
            draw_wall: for visualization, draw wall in the four direction if wall is marked True
                Parameters: current window

        Function:
            draw_graph: create a 2D List to hold vertices
                Parameters:
                    rows: number of rows
                    width: width of each row
"""
# Colors as status of vertices
WHITE = (255, 255, 255) # default
BLACK = (0, 0, 0) # wall
RED = (255, 0, 0) # visited
GREEN = (0, 255, 0) # open
YELLOW = (255, 255, 0) # path
ORANGE = (255, 165 ,0) # start
BLUE = (0, 0, 255) # end


class Vertex:
    def __init__(self, row, column, width, color=WHITE):
        self.row = row
        self.column = column
        self.color = color
        self.width = width
        self.walls = {'top': True, 'bottom': True, 'left': True, 'right': True}
        self.visited = False # for maze generation, flag True after being visited, to avoid using Set
        self.neighbors = []
        
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
    
    def set_visted(self):
        self.color = RED

    def set_wall(self):
        self.color = BLACK

    def set_path(self):
        self.color = YELLOW

    def reset_vertex(self):
        self.color = WHITE

    def reset_wall(self, position):
        self.walls[position] = False

    # call this after the maze has been generated to update neighbors list
    def add_neighbors(self, vert_list):
        self.neighbors = []
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


def draw_graph(rows, width):
        graph = []
        sub_width = width // rows
        for row in range(rows):
            graph.append([])
            for column in range(rows):
                graph[row].append(Vertex(row, column, sub_width))
        return graph


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
