""" The dijkstra module contains functions that implements dijkstra's algorithm to the maze."""

from vertex import *
from queue import PriorityQueue
from visualization import *

open_pq = PriorityQueue()
open_pq_set = set()
# visited = set()
dist_to = {}
edge_to = {}

def dijkstra(win, start, end, graph):
    # TODO: Parameters wait to be revised
    """Run main parts of the algorithm.
    Pseudocode:
    Add (start, 0) to the priority queue(PQ)
    For all other vertices, v, add(v, infinity) --> Add them when visiting
    while PQ is not empty:
        set current vertex p (smallest vertex in PQ)
        remove current vertex from PQ
        add current vertex to VISITED
        
        if current == end:
            construct_path()
            return

        change color of current vertex
        visit(all edges from p)
    """

    # Add the START vertex to the OPEN_PQ
    open_pq.put((0, start))
    open_pq_set.add(start)

    # Add all vertices to DIST_TO with infinity value
    all_vertices = graph.get_vert_list()
    dist_to = {v: float('inf') for row in all_vertices for v in row}
    dist_to[start] = 0
    
    while open_pq.not_empty():
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()

        # removes and returns the item with the lowest priority (smallest number).
        current = open_pq.get()[1]
        open_pq_set.remove(current)
        # visited.add(current)

        if current == end:
            construct_path()
            return True
        
        # Visit neighbors
        for neighbor in current.get_neighbors():
            relax(current, neighbor)
    
        draw_graph(win, graph)

        # Change color
        if current != start:
            current.set_visited()






def relax(current, neighbor):
    """Vist the neighbor of the vertex
    Pseudocode:
    parameters: current vertex: p, neighbor: q
    if q is in VISITED:
        return
    
    if dist_to(p) + 1 < dis_to(q):
        update dis_to[q] # dis_to stores the distance from the source to the vertex, key is the vertex, value is the distance
        update edge_to[q] = p # edge_to stores the edge, key is the current vertex, value is the prior vertex
        change priority of PQ for (q, dis_to[q])
        change color of q
    """
    if neighbor.is_visited() or neighbor.is_start():
        return
    
    if dist_to[current] + 1 < dist_to[neighbor]:
        dist_to[neighbor] = dist_to[current] + 1
        edge_to[neighbor] = current
        if neighbor not in open_pq_set:
            open_pq.put((dist_to[neighbor], neighbor))
            open_pq_set.add(neighbor)
        neighbor.set_open()


        

def construct_path(start, end):
    """Construct the final shortest path.
    Pseudocode:
    current = end
    while current != start:
        change color of the current
        find the prior vertex: current = edge_to[current]
    change color of the start
    return
    """
    current = end
    while current != start:
        current.set_path()
        current = edge_to[current]
        # TODO: PYGAME: draw()


def reset():
    open_pq = PriorityQueue()
    open_pq_set = set()
    # visited = set()
    dist_to = {}
    edge_to = {}