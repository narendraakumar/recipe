from dag import Node
class Graph(MixInObject):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections=None, directed=False,node_connection_list=[]):
        self.all_nodes = node_connection_list
        if connections==None:
            connections = [(pair[0].data, pair[1].data) for pair in node_connection_list]
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)
        self.dag = None

    def add_node(node:Node,previous_node,next_node):
    
        return True
        
    def get_node(self,name):
        for node_pair in self.all_nodes:
            for node in node_pair:
                if node.name==name:
                    return node
        else:
            return None


    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def show_graph(self):
        edge_list = []
        dot = Digraph()
        for node in self._graph:
            dot.node(node,f"this is node {node}")
            for c_node in self._graph[node]:
                dot.node(c_node,f"this is node {c_node}")
                edge_list.append(str(node+c_node))
        dot.edges(edge_list)
        return dot.render(view=True)
           



    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

if __name__ == '__main__':
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                   ('C', 'D'), ('E', 'F'), ('F', 'C')]
    g = Graph(connections, directed=True)
    pretty_print = pprint.PrettyPrinter()
    pretty_print.pprint(g._graph)
    print(g.find_path('A','D'))
    g.show_graph()