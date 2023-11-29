""" The dijkstra module contains functions that implements dijkstra's algorithm to the maze."""

import vertex
from queue import PriorityQueue
import pygame
import time


def dijkstra(draw, start, end, graph):
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
    # Update neighbor
    for row in graph:
        for v in row:
            v.add_neighbors(graph)
    
    open_pq = PriorityQueue()
    open_pq_set = set()
    dist_to = {}
    edge_to = {}
    
    # Add the START vertex to the OPEN_PQ
    open_pq.put((0, start))
    open_pq_set.add(start)

    # Add all vertices to DIST_TO with infinity value
    all_vertices = vertex.get_all_vertices(graph)
    dist_to = {v: float('inf') for v in all_vertices}
    dist_to[start] = 0
    
    while not open_pq.empty():
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()

        # removes and returns the item with the lowest priority (smallest number).
        current = open_pq.get()[1]
        open_pq_set.remove(current)
        # visited.add(current)

        if current == end:
            construct_path(draw, start, end, edge_to)
            return True
        
        # Change color
        if current != start:
            # time.sleep(0.5)
            current.set_visited()
        
        # Visit neighbors
        for neighbor in current.get_neighbors():
            relax(current, neighbor, edge_to, dist_to, open_pq, open_pq_set)
    
        draw()






def relax(current, neighbor, edge_to, dist_to, open_pq, open_pq_set):
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
        # time.sleep(0.5)
        neighbor.set_open()
        

def construct_path(draw, start, end, edge_to):
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
        draw()