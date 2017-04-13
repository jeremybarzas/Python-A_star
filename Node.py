'''Node object'''

import pygame

class Node(object):
    '''Node object'''

    def __init__(self, position):
        '''node constructor'''
        self.pos = position
        self.g = 0
        self.h = 0
        self.f = self.h + self.g
        self.walkable = True
        self.parent = None
        self.neighbors = []
        self.graph_index = 0

        # drawing vars
        size = 30
        self.width = size
        self.height = size
        self.posx = (5 + self.width) * self.pos[0] + 5
        self.posy = (5 + self.height) * self.pos[1] + 5
        self.screenpos = (self.posx, self.posy)
        self.surface = pygame.Surface((self.width, self.height))
        self.color = (0, 0, 0)

    def __getitem__(self, key):
        '''get position with index'''
        return self.pos[key]

    def draw(self, screen):
        ''' draw node to screen'''
        self.surface.fill(self.color)
        screen.blit(self.surface, self.screenpos)

    def set_neighbors(self, graph):
        '''set neighbors for a node'''
        right = [1, 0]
        top_right = [1, 1]
        top = [0, 1]
        top_left = [-1, 1]
        left = [-1, 0]
        bottom_left = [-1, -1]
        bottom = [0, -1]
        bottom_right = [1, -1]
        dirs = [right, top_right, top, top_left,
                left, bottom_left, bottom, bottom_right]
        for i in dirs:
            item1 = i[0] + self.pos[0]
            item2 = i[1] + self.pos[1]
            fetch_node = graph.get_node([item1, item2])
            if fetch_node:
                self.neighbors.append(fetch_node)

    def dist_between(self, neighbor):
        '''set g score '''
        if self.pos[0] == neighbor.pos[0] or self.pos[1] == neighbor.pos[1]:
            return 10
        else:
            return 14

    def print_info(self):
        '''print info'''
        line1 = "ID: " + str(self.graph_index)
        line2 = "  Position: " + str(self.pos[0]) + ',' + str(self.pos[1])
        print line1 + line2
