import json
from platform import node
import pprint
from collections import defaultdict
from uuid import uuid4

from graphviz import Digraph

class MixInObject(object):
    def __init__(self) -> None:
        pass

    def json(self,serialize=True):
        if serialize:
            return json.dumps(self.json(),default=MixInObject.json_serializer)
        else:
            return json.loads(json.dumps(self.__dict__,default=MixInObject.json_serializer))

    @staticmethod
    def json_serializer(obj):
        if isinstance(obj, MixInObject):
            return obj.json()
        return obj.__dict__

class Node(MixInObject):

    def __init__(self,node_id=None,previous_nodes=None,next_nodes=None,json_obj=None,**kwargs) -> None:
        super().__init__()
        self.node_class = kwargs.pop("node_class","")
        self.node_id = str(uuid4()) if node_id is None else node_id
        if not isinstance(previous_nodes,list):
            previous_nodes = [previous_nodes]
        if not isinstance(next_nodes,list):
            next_nodes = [next_nodes]

        self.previous_nodes = previous_nodes
        self.next_nodes = next_nodes
        kwargs.pop("node_id")
        self.__dict__.update(kwargs)
        if json_obj is not None:
            self.load(json_obj=json_obj)

    def load(self,json_obj):
        return self.__dict__.update(json_obj)

    def load_all_tasks(self):
        pass

