

class AggregateExec(Node):
    def __init__(self, node_id=None, previous_nodes=None, next_nodes=None, json_obj=None, **kwargs) -> None:
        super().__init__(node_id, previous_nodes, next_nodes, json_obj, **kwargs)
        self.node_class = "aggregate"

