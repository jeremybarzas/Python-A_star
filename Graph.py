'''Graph object'''

from Node import Node

class Graph(object):
    '''Graph object'''

    def __init__(self, size):
        '''constructor'''
        cols = size[0]
        rows = size[1]
        self.nodelist = []
        for i in range(0, cols):
            for j in range(0, rows):
                self.nodelist.append(Node([i, j]))
        for node in self.nodelist:
            node.graph_index = self.nodelist.index(node)
            node.set_neighbors(self)

    def get_node(self, searchfor):
        '''get a node by list [1,1]'''
        for node in self.nodelist:
            if node.pos == searchfor:
                return node

    def print_info(self):
        '''print node'''
        for node in self.nodelist:
            node.print_info()
