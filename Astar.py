'''Astar algorithim object'''

from AstarTestOne import getneighbors

def manhattan_distance(start, goal):
    '''manhattan distance heuristic'''
    x_dif = abs(goal[0] - start[0])
    y_dif = abs(goal[1] - start[1])
    return (x_dif + y_dif) * 10

def dist_between(start, neighbor):
    '''set g score '''
    if start[0] == neighbor[0] or start[1] == neighbor[1]:
        return 10
    else:
        return 14

def pathfind(start, goal, graph):
    '''the Astar search algorithim'''
    search_space = graph
    start.walkable = True
    goal.walkable = True
    openlist = []
    closedlist = []
    path = []
    openlist.append(start)
    openlist.sort(key=lambda x: x.f)
    while len(openlist) != 0:
        current = openlist[0]
        openlist.remove(current)
        closedlist.append(current)
        if current == goal:
            path = retrace(current)
            return path
        neighbors = getneighbors(current, search_space)
        for neighbor in neighbors:
            if neighbor in closedlist or not neighbor.walkable:
                continue
            tent_gcost = current.g + dist_between(current, neighbor)
            if neighbor not in openlist:
                neighbor.f = neighbor.g + neighbor.h
                openlist.append(neighbor)
            elif tent_gcost >= neighbor.g:
                continue
            neighbor.parent = current
            neighbor.g = tent_gcost
            neighbor.h = manhattan_distance(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
    return path

def retrace(node):
    '''reconstructs the path'''
    final_path = []
    iterator = node
    while iterator.parent is not None:
        final_path.append(iterator)
        iterator = iterator.parent
    final_path.append(iterator)
    return final_path
