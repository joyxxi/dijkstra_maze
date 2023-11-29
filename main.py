import dijkstra
import vertex
import visualization
import maze_generator
import pygame

WIDTH = 500
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Odyssey")

def main(win, width):
    ROWS = 20
    # Construct the graph
    graph = vertex.draw_graph(ROWS, WIDTH)

    # Start and End vertex. Assigned after maze generation.
    start = None
    end = None

    run = True
    # started = False

    while run:
        visualization.draw_graph(win, graph)

        # Loop through all the events that happened and check what they are
        for event in pygame.event.get():
            # When press the QUIT, stop running the game
            if event.type == pygame.QUIT:
                run = False

            # Once we started the algorithm, don't want user to press anything, unless the quit button    
            # if started:
            #     continue

            if pygame.mouse.get_pressed()[0]: # Left
                # # Run maze
                maze = maze_generator.Maze(ROWS, ROWS)
                maze.create_solution_path()
                graph = maze.maze_for_return(width)

                    
                start_x, start_y = maze.start
                # start = graph[start_x][ROWS - 1 - start_y]
                start = graph[start_x][start_y]
                start.set_start()
                end_x, end_y = maze.end
                # end = graph[end_x][ROWS - 1 - end_y]
                end = graph[end_x][end_y]
                end.set_end()

                # start = graph[0][0]
                # start.set_start()
                # end = graph[3][3]
                # end.set_end()
                # start.walls['bottom'] = False
                # graph[1][0].walls['top'] = False
                # start.walls['right'] = False
                # graph[0][1].walls['left'] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # Run Dijkstra
                    dijkstra.dijkstra(lambda: visualization.draw_graph(win, graph), start, end, graph)
    # Exit the pygame window
    pygame.quit()


main(WINDOW, WIDTH)