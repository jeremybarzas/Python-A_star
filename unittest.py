'''Unit testing for astar algorithim'''

import pygame
from Astar import Grid
from Astar import AStar


def unit_test():
    '''unit test'''
    print "\nBegin unit test\n"
    grid = Grid([10, 10])
    grid.print_info()

    grid.nodelist[26].walkable = False
    grid.nodelist[36].walkable = False
    grid.nodelist[46].walkable = False
    grid.nodelist[56].walkable = False
    grid.nodelist[63].walkable = False
    grid.nodelist[64].walkable = False
    grid.nodelist[65].walkable = False
    grid.nodelist[66].walkable = False

    astar = AStar()
    astar.pathfind(grid.nodelist[0], grid.nodelist[99])


if __name__ == "__main__":
    unit_test()
