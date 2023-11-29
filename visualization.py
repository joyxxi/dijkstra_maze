import pygame
from vertex import *


def draw_vertex_wall(win, graph):
    """ Draw the wall surrounding the vertex after to construct the maze."""
    for row in graph:
        for v in row:
            width = v.width
            y = v.row * width
            x = v.column * width
            thickness = 4

            # draw top wall
            if v.walls['top']:
                pygame.draw.line(win, BLACK, (x, y), (x + width, y), thickness)
            # draw right wall
            if v.walls['right']:
                pygame.draw.line(win, BLACK, (x + width, y), (x + width, y + width), thickness)
            # draw bottom wall
            if v.walls['bottom']:
                pygame.draw.line(win, BLACK, (x + width, y + width), (x, y + width), thickness)
            # draw left wall
            if v.walls['left']:
                pygame.draw.line(win, BLACK, (x, y + width), (x, y), thickness)
    
    # pygame.display.update()


def draw_vertex_color(win, graph):
    """ Fill the color of each vertex."""
    for row in graph:
        for v in row:
            width = v.width
            y = v.row * width
            x = v.column * width
            pygame.draw.rect(win, v.color, (x, y, width, width))
    
    # pygame.display.update()

def draw_graph(win, graph):
    """ Draw the graph. Apply it everytime we need to update the graph."""
    win.fill(WHITE)
    draw_vertex_color(win, graph)
    draw_vertex_wall(win, graph)
    pygame.display.update()
    
