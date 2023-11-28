import random
from collections import deque
import collections
from enum import Enum
from vertex import Vertex


# Note: Adjust console font to get the maze to look right

class Node:

    class PathState(Enum):
        CLEAR = 0
        VISITED = 1

    def __init__(self):
        self.next_in_solution = None
        self.prev_in_path = None
        self.state = self.PathState.CLEAR


class Maze:

    class NoSolutionGenerated(Exception):
        pass

    class Method(Enum):
        STACK = 0
        RANDOM = 1

    open_char = " "
    h_block_char = "\u2588"
    v_block_char = "\u2588"
    sol_char = "*"

    def __init__(self, width=10, height=10):
        self._h_walls = [[1] * (height) for _ in range(width)]
        self._v_walls = [[1] * height for _ in range(width)]
        self._grid = [[Node() for _ in range(height + 1)] for _ in range(width + 1)]
        self._width = width
        self._height = height
        self._start = None
        self._end = None
        self._solution_path = None

    @property
    def start(self):
        return self._start, 0

    @property
    def end(self):
        return self._end, self._height - 1

    def _build_solution_path(self):
        self._solution_path = [(self._end, self._height - 1)]
        while self._solution_path[-1] != (self._start, 0):
            curr_x, curr_y = self._solution_path[-1]
            next_pos = self._grid[curr_x][curr_y].prev_in_path
            self._solution_path.append(next_pos)
        self._solution_path.reverse()

    @property
    def solution_path(self):
        if not self._solution_path:
            raise Maze.NoSolutionGenerated
        return self._solution_path

    def print_maze(self, with_solution=False):
        top_line = self.h_block_char
        for pos in range(self._width):
            top_line += self.open_char if pos == self._end \
                else self.h_block_char
            top_line += self.h_block_char
        print(top_line)
        for y in range(self._height - 1, -1, -1):

            # Print horizontal walls (except the first time)
            if y < self._height - 1:
                row_line = self.h_block_char
                for x in range(0, self._width):
                    row_line += self.h_block_char if self._h_walls[x][y] \
                        else self.open_char
                    row_line += self.h_block_char
                print(row_line)

            # Print vertical walls and path
            row_line = self.v_block_char
            for x in range(0, self._width):
                if with_solution and (x, y) in self._solution_path:
                    row_line += self.sol_char
                else:
                    row_line += self.open_char
                if x < self._width - 1:
                    row_line += self.v_block_char if self._v_walls[x][y] \
                        else self.open_char
            row_line += self.v_block_char
            print(row_line)
        bot_line = self.h_block_char
        for pos in range(self._width):
            bot_line += self.open_char if pos == self._start \
                else self.h_block_char
            bot_line += self.h_block_char
        print(bot_line)

    def valid_position(self, x, y):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return False
        return True

    def is_wall(self, curr_x, curr_y, prop_x, prop_y):
        if prop_x < curr_x:
            if self._v_walls[prop_x][prop_y]:
                return True
        if curr_x < prop_x:
            if self._v_walls[curr_x][prop_y]:
                return True
        if prop_y < curr_y:
            if self._h_walls[prop_x][prop_y]:
                return True
        if curr_y < prop_y:
            if self._h_walls[prop_x][curr_y]:
                return True
        return False

    def break_wall(self, curr_x, curr_y, prop_x, prop_y):
        if prop_x < curr_x:
            self._v_walls[prop_x][prop_y] = 0
        if curr_x < prop_x:
            self._v_walls[curr_x][prop_y] = 0
        if prop_y < curr_y:
            self._h_walls[prop_x][prop_y] = 0
        if curr_y < prop_y:
            self._h_walls[prop_x][curr_y] = 0

    def maze_for_return(self):
        """Create and return a 2D array of Vertex objects
           based on the maze that was created.
        """
        ret_maze = []
        # starting from the bottom row
        for x in range(self._width):
            temp = []
            # moving up
            for y in range(self._height):
                new_vertex = Vertex(row=x, column=y, width=1)
                if self.valid_position(x + 1, y):
                    if not self.is_wall(x, y, x + 1, y):
                        new_vertex.reset_walls('right')
                if self.valid_position(x - 1, y):
                    if not self.is_wall(x, y, x - 1, y):
                        new_vertex.reset_walls('left')
                if self.valid_position(x, y + 1):
                    if not self.is_wall(x, y, x, y + 1):
                        new_vertex.reset_walls('top')
                if self.valid_position(x, y - 1):
                    if not self.is_wall(x, y, x, y - 1):
                        new_vertex.reset_walls('bottom')
                temp.append(new_vertex)
            ret_maze.append(temp)
        return ret_maze

    def create_solution_path(self, method=Method.RANDOM):

        def random_move(curr_pos):
            next_pos = [*curr_pos]
            move = random.randint(0, 3)
            if move == 0:
                next_pos[0] += 1
            elif move == 1:
                next_pos[0] -= 1
            elif move == 2:
                next_pos[1] += 1
            else:
                next_pos[1] -= 1
            return tuple(next_pos)

        def paths_remain(curr_x, curr_y):
            # Top row always has a path
            if curr_y == self._height - 1:
                return True
            for choice in [(curr_x + i, curr_y + j) for i, j in
                           [[-1, 0], [0, -1], [1, 0], [0, 1]]]:
                if choice in unvisited_set:
                    return True
            return False

        self._start = self._width // 2
        if method == self.Method.STACK:
            backtrack_stack = deque()
        else:
            backtrack_stack = list()

        backtrack_stack.append((self._start, 0))
        unvisited_set = {(x, y) for x in range(self._width)
                         for y in range(self._height)}
        while True:
            if method == self.Method.RANDOM:
                current_pos = random.choice(backtrack_stack)
                backtrack_stack.remove(current_pos)
            else:
                current_pos = backtrack_stack.pop()
            # It's possible that this node has been boxed in
            if not paths_remain(*current_pos):
                continue
            unvisited_set.discard(current_pos)
            proposed_next = random_move(current_pos)

            if proposed_next[1] == self._height:
                self._end = current_pos[0]
                self._grid[current_pos[0]][current_pos[1]].next_in_solution = \
                    proposed_next
                break

            if tuple(proposed_next) not in unvisited_set:
                backtrack_stack.append(current_pos)
                continue
            else:
                # We are forging new ground, tear down the wall
                self.break_wall(*current_pos, *proposed_next)
                self._grid[current_pos[0]][current_pos[1]].next_in_solution = \
                    proposed_next
                self._grid[proposed_next[0]][proposed_next[1]].prev_in_path = \
                    current_pos
                if paths_remain(*current_pos):
                    backtrack_stack.append(current_pos)
                backtrack_stack.append(proposed_next)
                unvisited_set.discard(proposed_next)

        # Now fill in the rest of the routes
        while unvisited_set:
            iterable_version = list(unvisited_set)
            for node in iterable_version:
                proposed_next = random_move(node)
                if self.valid_position(*proposed_next) and \
                        proposed_next not in unvisited_set:
                    self.break_wall(*node, *proposed_next)
                    unvisited_set.discard(node)

        self._build_solution_path()


def main():
    my_maze = Maze(5, 5)
    my_maze.create_solution_path()
    my_maze.print_maze(True)
    ret_maze = my_maze.maze_for_return()
    for row in ret_maze:
        for v in row:
            print(v.row, v.column)
            print(v.walls.items())
    print()
    print(ret_maze)
    print(f"Start = {my_maze.start}")
    print(f"End = {my_maze.end}")
    print()
    print(my_maze.solution_path)

    

if __name__ == "__main__":    
    main()
