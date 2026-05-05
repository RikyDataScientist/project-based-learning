class graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))

    def p_graph(self):
        for u, v in self.graph.items():
            print(u, ' --> ', v)
        print()

    def dfs(self, start):
        order = {
            'A': 0, 'E': 1, 'I': 2, 'M': 3, 'N': 4,
            'K': 5, 'O': 6, 'P': 7, 'L': 8, 'H': 9,
            'D': 10, 'C': 11, 'B': 12, 'F': 13, 'G': 14, 'J': 15
        }
        visited = set()
        stack = [start]
        lst = []

        while stack:
            node = stack.pop()
    
            if node not in visited:
                lst.append(node)
                visited.add(node)

                neighbors = sorted(
                    self.graph[node],
                    key=lambda x: order[x[0]],
                    reverse=True
                )

                for neighbor, _ in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return ' --> '.join(lst)

    def bfs(self, start):
        visited = set([start])
        queue = [start]
        res = []

        while queue:
            node = queue.pop(0)
            res.append(node)
            for neighbor, _ in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return " --> ".join(res)

if __name__ == '__main__':
    g = graph()

    g.add_edge('A', 'B')
    g.add_edge('A', 'F')
    g.add_edge('A', 'E')
    g.add_edge('B', 'C')
    g.add_edge('B', 'F')
    g.add_edge('E', 'F')
    g.add_edge('E', 'I')
    g.add_edge('I', 'F')
    g.add_edge('I', 'J')
    g.add_edge('I', 'M')
    g.add_edge('I', 'N')
    g.add_edge('M', 'N')
    g.add_edge('N', 'K')
    g.add_edge('J', 'K')
    g.add_edge('J', 'G')
    g.add_edge('K', 'G')
    g.add_edge('K', 'O')
    g.add_edge('G', 'C')
    g.add_edge('G', 'D')
    g.add_edge('G', 'L')
    g.add_edge('C', 'D')
    g.add_edge('D', 'H')
    g.add_edge('L', 'H')
    g.add_edge('L', 'P')
    g.add_edge('O', 'P')

    g.p_graph()
    print('DFS Result:')
    print(g.dfs('A'))
    print()
    print('BFS Result:')
    print(g.bfs('A'))
