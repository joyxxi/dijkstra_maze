""" The dijkstra module contains functions that implements dijkstra's algorithm to the maze."""

def dijkstra():
    """Run main parts of the algorithm.
    Pseudocode:
    Add (start, 0) to the priority queue(PQ)
    For all other vertices, v, add(v, infinity)
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
    # TODO

def visit():
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
    # TODO

def construct_path():
    """Construct the final shortest path.
    Pseudocode:
    current = end
    while current != start:
        change color of the current
        find the prior vertex: current = edge_to[current]
    change color of the start
    return
    """
    # TODO