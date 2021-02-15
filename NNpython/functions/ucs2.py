from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.visited = []
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]

    def ucs(self, graph, start, goal):
        queue = PriorityQueue()
        queue.put(0, start)

        while queue:
            cost = queue.get()
            node = queue.get()
            if node not in self.visited:
                self.visited.append(node)

                if node == goal:
                    return
                for i in graph.neighbors[node]:
                    if i not in self.visited:
                        total_cost = cost + graph.get_cost(node, i)
                        queue.put((total_cost, i))
