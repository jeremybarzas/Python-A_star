'''AStar algorithim'''


class Node(object):
    '''Node object'''

    def __init__(self, position):
        '''node constructor'''
        self.pos = position
        self.gcost = 0
        self.hcost = 0
        self.fcost = 0
        self.walkable = True
        self.parent = None
        self.neighbors = []
        self.graph_index = 0

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
        '''get g score '''
        if self.pos[0] == neighbor.pos[0] or self.pos[1] == neighbor.pos[1]:
            return 10
        else:
            return 14

    def print_info(self):
        '''print info'''
        line1 = "ID: " + str(self.graph_index)
        line2 = "  Position: " + str(self.pos[0]) + ',' + str(self.pos[1])
        print line1 + line2


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


class AStar(object):
    '''AStar algorithim'''

    def __init__(self):
        '''constructor'''

    def manhattan_distance(self, start, goal):
        '''manhattan distance heuristic'''
        x_dif = abs(start.pos[0] - goal.pos[0])
        y_dif = abs(start.pos[1] - goal.pos[1])
        return (x_dif + y_dif) * 10

    def pathfind(self, start, goal):
        '''the astar search algorithim'''
        print "\nStart Node:"  # DEBUG STUFF
        start.print_info()  # DEBUG STUFF
        print "Goal Node:"  # DEBUG STUFF
        goal.print_info()  # DEBUG STUFF
        openlist = []
        closedlist = []
        current = start
        openlist.append(current)
        while openlist.count != 0:
            openlist.sort(key=lambda x: x.fcost)
            current = openlist[0]
            if current == goal:
                print "\nCurrent Node: "  # DEBUG STUFF
                current.print_info()  # DEBUG STUFF
                return self.retrace(current)
            openlist.remove(current)
            closedlist.append(current)
            for neighbor in current.neighbors:
                if neighbor in closedlist or not neighbor.walkable:
                    continue
                tent_gcost = current.gcost + current.dist_between(neighbor)
                if neighbor not in openlist:
                    openlist.append(neighbor)
                elif tent_gcost > neighbor.gcost:
                    continue
                neighbor.parent = current
                neighbor.gcost = tent_gcost
                neighbor.hCost = self.manhattan_distance(neighbor, goal)
                neighbor.fCost = neighbor.gcost + neighbor.hcost
        return False

    def retrace(self, node):
        '''reconstructs the path'''
        print "Retrace has been called"  # DEBUG STUFF
        print "Path that was taken:"  # DEBUG STUFF
        final_path = []
        iterator = node
        while iterator is not None:
            final_path.append(iterator)
            iterator = iterator.parent
        for node in final_path:  # DEBUG STUFF
            node.print_info()  # DEBUG STUFF
        return final_path
