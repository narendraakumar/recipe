

class ConditionExec(Node):
    def __init__(self, node_id=None, previous_nodes=None, next_nodes=None, json_obj=None,input_data=None, **kwargs) -> None:
        super().__init__(node_id, previous_nodes, next_nodes, json_obj, **kwargs)
        self.input_data = self.output_data = input_data
        self.node_class = "condition"