from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.visited = []
        self.edges = {}
        self.weights = {}

    def ucs_weight(self, from_node, to_node, weights='weights'):
        return weights.get((from_node, to_node), 10e100) if weights else 1

    def ucs(self, graph, start, end, weights=None):
        queue = PriorityQueue()
        queue.put(0, start)
        self.visited = []

        while True:
            if queue.empty():
                raise Exception("No way exception")

            ucs_w = queue.get()
            current_node = queue.get()
            self.visited.append(current_node)

            if current_node == end:
                print('already there')

            for node in graph[current_node]:
                if node not in self.visited:
                    queue.put((ucs_w + self.ucs_weight(current_node, node), node))
