from collections import deque


INF = float("inf")


class Graph:
    def __init__(self, entrances, exits, path):
        self.graph = [list(row) for row in path]
        self.nodes_number = len(self.graph)
        self.max_flow = None

        self.entrance = self.nodes_number
        self.exit = self.nodes_number + 1

        for row in range(self.nodes_number):
            self.graph[row].append(0)
            self.graph[row].append(INF if row in exits else 0)

        self.nodes_number += 2

        self.graph.append([(INF if x in entrances else 0) for x in range(self.nodes_number)])
        self.graph.append([0] * self.nodes_number)

    def bfs(self):
        visited = set()
        deq = deque()
        deq.append((self.entrance, [self.entrance]))

        while len(deq) > 0:
            current, path = deq.popleft()
            if current == self.exit:
                return path

            for i in range(self.nodes_number):
                if i not in visited and self.graph[current][i] > 0:
                    visited.add(i)
                    new_path = list(path)
                    new_path.append(i)
                    deq.append((i, new_path))

        return None

    def get_max_flow(self):
        if self.max_flow is None:
            max_flow = 0

            while True:
                shortest_path = self.bfs()

                if shortest_path is None:
                    break

                flow = INF
                for i in range(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    flow = min(flow, self.graph[node_from][node_to])

                for i in range(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    self.graph[node_from][node_to] -= flow
                    self.graph[node_to][node_from] += flow

                max_flow += flow

            self.max_flow = max_flow

        return self.max_flow


def answer(entrances, exits, path):
    g = Graph(entrances, exits, path)
    return g.get_max_flow()

print(answer([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))    