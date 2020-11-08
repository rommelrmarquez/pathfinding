class Node:
    def __init__(self, parent=None, position=None):
        self.position = position
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f'({self.position[0]}, {self.position[1]})'

    def __repr__(self):
        return f'({self.position[0]}, {self.position[1]})'


def astar_finder(maze, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_nodes = [start_node]
    closed_nodes = []

    while open_nodes:
        current_node = open_nodes[0]
        current_idx = 0
        for idx, node in enumerate(open_nodes):
            if node.f < current_node.f:
                current_node = node
                current_idx = idx

        open_nodes.pop(current_idx)
        closed_nodes.append(current_node)

        # check if current_node is the end_node
        # if yes, traverse the path from beginning
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Get children nodes
        children = []
        allowed_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in allowed_moves:
            new_x = (current_node.position[0] + x)
            new_y = (current_node.position[1] + y)

            # check if new position is in the maze
            if (new_x > (len(maze) - 1) or new_x < 0 or
               (new_y > len(maze[new_x]) - 1) or new_y < 0):
               continue

            # check if new position is not a wall
            if maze[new_x][new_y] != 0:
                continue

            new_node = Node(current_node, (new_x, new_y))
            children.append(new_node)

        # Loop through children
        for child in children:
            if child in closed_nodes: continue

            # compute metrics
            child.g = current_node.g + 1
            child.h = (((child.position[0] - child.position[0]) ** 2) +
                       ((child.position[1] - child.position[1]) ** 2))
            child.f = child.g + child.h


            # check if child is already in open_nodes and
            # g is greater than the found node
            try:
                found_node = open_nodes[open_nodes.index(child)]
                if child.g > found_node.g:
                    continue
            except ValueError:  # not in open_nodes
                pass

            # add child to open_nodes
            open_nodes.append(child)


def main():

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
    maze2 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    no_way = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    print('\nTRAVEL PATH: ', astar_finder(maze, (0, 0), (7, 6)))

    print('\nTRAVEL PATH: ', astar_finder(no_way, (0, 0), (7, 6)))

    print('\nTRAVEL PATH: ', astar_finder(maze2, (0, 0), (9, 9)))


if __name__ == '__main__':
    main()
