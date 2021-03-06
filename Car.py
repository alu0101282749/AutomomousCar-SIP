from heapq import *
from math import sqrt
import numpy
import random


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    # overwite the qual method to get a match when the positions are qeual
    def __eq__(self, other):
        return self.position == other.position

    # overwrite the compare itselfe method so heapq will take the f-value of the Node to sort by
    def __lt__(self, other):
        return self.f < other.f

class Map():
    def __init__(self, map_size=(10,10), start=(0,0), end = (6,6), obstacles_percent=0):
        self.m_size = map_size
        self.map = numpy.zeros(shape=map_size)

        self.m_obstacles_percent = obstacles_percent
        self.create_map()

    # overwrite str method so the map can be printet
    def __str__(self):
        to_ret = str(self.map)
        to_ret = " " + to_ret[1:-1]
        return to_ret

    def create_map(self):
        #
        obst = self.m_size[0] * self.m_size[1] * self.m_obstacles_percent / 100
        while obst:
            x = random.randint(0,self.m_size[0]-1)
            y = random.randint(0, self.m_size[1] - 1)
            if self.map[x][y] == 0:
                self.map[x][y] = 1
            obst -=1




class Nav(object):
    """docstring for Map"""

    def __init__(self, ):
        self.size = size
        self.start = start
        self.end = end
        self.obstacles = obstacles
        self.maze = \
           [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.path = []

    def heuristics(node, end_node, h):
        if h == 0:
            return sqrt((node.position[0] - end_node.position[0]) ** 2) + (
                        (node.position[1] - end_node.position[1]) ** 2)
        elif h == 1:
            return (abs(node.position[0] - end_node.position[0])) + abs((node.position[1] - end_node.position[1]))

    def astar(maze, start, end, h):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        heappush(open_list, start_node)

        # Loop until you find the end
        while open_list:

            # Get the current node
            current_node = heappop(open_list)

            # Pop current off open list, add to closed list
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                                 (1, 1)]:  # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the g, h and f values
                child.g = current_node.g + 1
                child.h = heuristics(child, end_node, h)  # h: choose heuristic case
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

class AutonmCar(object):
    """docstring for AutonmCar"""
    def __init__(self):
        self.ac_map = None


    def getUserInput(self):

        print("Map dimensions m x n(e.g. 10x10):")
        n = int(input(' type in n (width) value:'))
        m = int(input(' type in m (bright) value:'))
        ac_map_size = (n,m)
        print(' Map will be {} x {}\n'.format(ac_map_size[0], ac_map_size[1]))
        # for testing here
        self.ac_map = Map(ac_map_size,(1,2),(5,5), 50)
        print (self.ac_map)




def main():




    car1 = AutonmCar()
    car1.getUserInput()

    #Todo: print_map:           ok
    #Todo: Userimput            ok
    #Todo: create map method    ok
    #Todo: print way
    #Todo: make astar to work


    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    #path = astar(maze, start, end, 1)
    #print("sortest-path:", path)
    # maze[0][0]= 1
    #print("\n")
    #print("map:\n", maze)

    a = AutonmCar()


if __name__ == '__main__':
    main()