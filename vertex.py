""" class Vertex
    Attributes:
        id: id of the vertex
        neighbors: list of neighbors of the vertex
        x: position of row
        y: position of colomn
        color: color/status of the vertex, default to white
        width: width of the vertex

    Methods:
        get_pos: get position (x, y)
        is_open, is_closed, is_barrier, is_start, is_end, is_path: return True if the vertex is of the status
        make_open, make_closed, make_barrier, make_start, make_end, make_path: change the status
        reset_grid: change vertex to the default status
"""


# Colors as flag
WHITE = (255, 255, 255) # default
RED = (255, 0, 0) # closed/visited
GREEN = (0, 255, 0) # open: it may not be used
ORANGE = (255, 165 ,0) # start
BLUE = (0, 255, 0) # end
BLACK = (0, 0, 0) # barrier
YELLOW = (255, 255, 0) # path


class Vertex:
    def __init__(self, key, row, col, width, total_rows):
        self.id = key
        self.neighbors = []
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
        self.prev_nbr = None # does Djikstra need this?

    def get_pos(self):
        return (self.row, self.col)
    
    def is_open(self):
        return self.color == GREEN
    
    def is_closed(self):
        return self.color == RED
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == BLUE
    
    def is_path(self):
        return self.color == YELLOW

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_open(self):
        self.color = GREEN
    
    def make_closed(self):
        self.color = RED

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = YELLOW

    def reset_grid(self):
        self.color = WHITE

    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return str(self.id) + 'connects to: ' + str([x.id for x in self.neighbors])
    
    """ to do
        check if add_neighbors() is correct
        def get_neighbors(self):
        def make_prev_nbr(self, nbr):
            self.prev_nbr = nbr
        def get_prev_nbr(self):
    """