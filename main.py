from dijkstra import *
from graph import *
from vertex import *
from visualization import *

WIDTH = 1000
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Odyssey")

def main(win, width):
    ROWS = 10

    # Construct the graph
    graph = Graph(ROWS)
    graph = graph.draw_graph(width) # TODO: wait to be revised

    # Start and End vertex. Assigned after maze generation.
    start = None
    end = None

    # If we are running the main loop
    run = True
    # If we actually started the algorithm
    started = False

    while run:
        draw_graph(win, graph)

        # Loop through all the events that happened and check what they are
        for event in pygame.event.get():
            # When press the QUIT, stop running the game
            if event.type == pygame.QUIT:
                run = False


            # Once we started the algorithm, don't want user to press anything, unless the quit button    
            if started:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    # Run maze
                    # TODO
                    # Update neighbors
                    for row in graph:
                        for v in row:
                            v.add_neighbors(graph) # TODO: Need to be revised

                    # Run Dijkstra
                    dijkstra(win, start, end, graph) #TODO: Parameters wait to be revised
    # Exit the pygame window
    pygame.quit()


main(WINDOW, WIDTH)