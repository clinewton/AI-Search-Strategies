class GreedyBFS:
    def __init__(self):
        self.visited = []
        self.end_search = False

    def gbfs(self, graph, start_node, end_node):
        queue = []
        queue.append(start_node)
        # since we have visited the start node we add it to the visited list
        self.visited.append(start_node)
        while queue and not self.end_search:
            s = queue.pop(0)

            for i in list(graph[s]):
                if i not in self.visited:
                    print("go to", i, ".", end="\n")
                    if i is end_node:
                        print("you have arrived at ", i, "which is your destination")
                        self.visited.append(i)
                        self.end_search = True
                        break
                    else:
                        queue.append(i)
                        self.visited.append(i)
