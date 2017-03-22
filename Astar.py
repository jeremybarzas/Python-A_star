'''Astar algorithim object'''

class Astar(object):
    '''Astar algorithim'''

    def __init__(self):
        '''constructor'''

    def manhattan_distance(self, start, goal):
        '''manhattan distance heuristic'''
        x_dif = abs(start.pos[0] - goal.pos[0])
        y_dif = abs(start.pos[1] - goal.pos[1])
        return (x_dif + y_dif) * 10

    def pathfind(self, start, goal):
        '''the Astar search algorithim'''
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
                neighbor.hcost = self.manhattan_distance(neighbor, goal)
                neighbor.fcost = neighbor.gcost + neighbor.hcost
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
