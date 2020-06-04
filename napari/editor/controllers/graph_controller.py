class GraphController:
    @staticmethod
    def connections(graph: 'Graph') -> ['Connection']:
        return graph.connections

    @staticmethod
    def nodes(graph: 'Graph') -> ['Node']:
        return graph.nodes

    @staticmethod
    def connect(graph: 'Graph', connection: 'Connection'):
        graph.connect(connection)
