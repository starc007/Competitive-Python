class Node(object):
    def __init__(self, identity, x, y):
        self.neighbours = []
        self.identity = identity
        self.coordinates = (x, y)

    def addNeighbour(self, node_key):
        self.neighbours.append(node_key)

class Graph(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.passable_walls = set()
        self.nodes = {}

    def create(self):
        length = len(self.matrix)
        for row in range(length):
            for col in range(length):
                identity = 0
                if self.matrix[row][col] == 1:
                    identity = 1

                node = Node(identity, row, col)

                # Get the neighbours
                if self._hasNeighbour(row - 1, col): # Is the top cell there?
                    node.addNeighbour((row - 1, col))

                if self._hasNeighbour(row + 1, col): # Is the bottom cell there?
                    node.addNeighbour((row + 1, col))

                if self._hasNeighbour(row, col - 1): # Is the left cell there?
                    node.addNeighbour((row, col - 1))

                if self._hasNeighbour(row, col + 1): # Is the right cell there?
                    node.addNeighbour((row, col + 1))

                self.nodes[(row, col)] = node

    def getWalls(self):
        length = len(self.matrix)
        traversed_walls = 0
        for row in range(length):
            for col in range(length):
                if self.matrix[row][col] == 1:
                    self.passable_walls.add((row, col))

    def findShortestPath(self, start, end, passable_wall, path=set()):
        path.add(start)
        if start == end:
            return path

        if start not in self.nodes:
            return None

        shortest = None
        for node in self.nodes[start].neighbours:
            if node not in path and (self.nodes[node].identity == 0 or self.nodes[node].coordinates == passable_wall):
                curr_path = set(path)
                new_path = self.findShortestPath(self.nodes[node].coordinates, end, passable_wall, curr_path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path

        return shortest

    def _hasNeighbour(self, row, col):
        length = len(self.matrix)
        if row < 0 or col < 0 or row >= length or col >= length:
            return False

        return True

def solution(map):
    graph = Graph(map)

    shortest = None
    matrix_length = len(map)
    start_node = (0, 0)
    exit_node = (matrix_length - 1, matrix_length - 1)
    graph.create()
    graph.getWalls()
    for wall in graph.passable_walls:
        curr_path = graph.findShortestPath(start_node, exit_node, wall, path=set())
        if curr_path is not None:
            if shortest is None:
                shortest = len(curr_path)
            else:
                if len(curr_path) < shortest:
                    shortest = len(curr_path)

    return shortest

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))    