'''Unit testing for astar algorithim'''

import pygame
import Astar
from Graph import Graph

def unit_test():
    '''unit test'''
    print "\nBegin unit test\n"
    pygame.init()
    pygame.display.set_caption("A* Pathfinding")
    # colors to be used
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (125, 125, 125)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    # drawing variables
    pad = (5, 5)
    rows = 10
    cols = 10
    width = 30
    height = 30
    screen_width = cols * (pad[0] + width) + pad[1]
    screen_height = rows * (pad[0] + height) + pad[1]
    screen = pygame.display.set_mode((screen_width, screen_height))
    # this is the graph of nodes
    search_space = Graph([rows, cols])
    search_space.print_info()
    # these are the unwalkable nodes
    search_space.nodelist[26].walkable = False
    search_space.nodelist[36].walkable = False
    search_space.nodelist[46].walkable = False
    search_space.nodelist[56].walkable = False
    search_space.nodelist[63].walkable = False
    search_space.nodelist[64].walkable = False
    search_space.nodelist[65].walkable = False
    search_space.nodelist[66].walkable = False
    # this is the node to start from
    start = search_space.nodelist[0]
    start.color = green
    # this is the goal node to travel to
    goal = search_space.nodelist[99]
    goal.color = red
    # this is the path taken from start to goal
    path_taken = []
    # this is the A * algorithim being called and its return value being store in path_taken
    path_taken = Astar.pathfind(start, goal, search_space)
    # variable to control the loop
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
        screen.fill(white)
        # colors and prints all nodes in the graph
        for node in search_space.nodelist:
            if node.walkable is False:
                node.color = black
            else:
                node.color = blue
            node.draw(screen)
        # colors and prints the nodes in the path taken to gray
        for node in path_taken:
            if node == start:
                node.color = green
            elif node == goal:
                node.color = red
            else:
                node.color = gray
            node.draw(screen)
        # update function
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    unit_test()
