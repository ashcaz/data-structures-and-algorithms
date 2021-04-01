class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start, end, weight=1):
        if start not in self._adjacency_list:
            raise KeyError("Start Vertex not in Graph")
        if end not in self._adjacency_list:
            raise KeyError("End Vertex not in Graph")
        edge = Edge(end, weight)
        adjacencies = self._adjacency_list[start]
        adjacencies.append(edge)

    def get_nodes(self):
        if self._adjacency_list == {}:
            return None
        else:
            nodes = [*self._adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value

            return nodes

    def get_neighbors(self, node):

        nodes = [*self._adjacency_list]

        print(nodes)

        for i in range(len(nodes)):
            if nodes[i].value == node:
                adjacencies = self._adjacency_list[nodes[i]]

                print(adjacencies)

                adjacencies_with_weight = [
                    adjacencies[i].vertex.value,
                    adjacencies[i].weight,
                ]

                return adjacencies_with_weight
            else:
                raise KeyError("The node you enteted does not exist")

    def size(self):
        return len(self._adjacency_list)

    def breadth_first(self, starting_node):
        pass


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
