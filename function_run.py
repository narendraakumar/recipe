class FunctionExec(Node):
    def __init__(self, node_id=None, previous_nodes=None, next_nodes=None, input_data=None, output_data=None, **kwargs) -> None:
        super().__init__(node_id, previous_nodes, next_nodes, **kwargs)
        self.input_data = input_data
        self.output_data = output_data
        self.node_class = "function"
        self.name = kwargs.pop("name","")
