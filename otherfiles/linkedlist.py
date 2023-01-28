#linked list

class LinkedList:
    def __init__(self,node_data=None) -> None:
        self.head = None
        if node_data is not None:
            self.head = Node(node_data.pop(0))
            node = self.head
            for data in node_data:
                node.next = Node(data)
                node = node.next
            


    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data) if node.name is None else node.name)
            node = node.next
        # nodes.append(None)
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node.next is not None:
            yield node
            node = node.next
        yield node

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self,node):
        node_ = self.head
        while node_.next is not None:
            node_ = node_.next
        node_.next = node

    def add_after(self,n,node):
        node_ = self.head
        while node_.data != n:
            node_ = node_.next

        node.next = node_.next
        node_.next = node
        

    def add_before(self,n,node):
        node_ = self.head
        while node_.data != n:
            prious_node = node_
            node_ = node_.next
        node.next = node_
        prious_node.next = node

    def remove_node(self,n):
        node_ = self.head
        while node_.data != n:
            previous_node = node_
            node_ = node_.next
        previous_node.next = node_.next

    def get_ele(self,i):
        node_ = self.head
        j = 0
        while i != j:
            j+=1
            node_ = node_.next
        return node_

    def __len__(self):
        node_ = self.head
        j = 1
        while node_.next != None:
            j+=1
            node_ = node_.next
        return j

    def reverse(self):
        current_node_ = self.head
        prev_node = None
        while current_node_ != None:
            next_node = current_node_.next
            current_node_.next = prev_node
            prev_node = current_node_
            current_node_ = next_node
        self.head = prev_node





class Node:
    def __init__(self,data,name=None) -> None:
        self.data = data
        self.next = None
        self.name = name 

    def __repr__(self) -> str:
        return str(self.data)

llist = LinkedList(node_data=[1,2,3,4,5])
# llist.add_first(Node(data=6))
# llist.add_last(Node(data=7))
# llist.add_after(3,Node(8))
# llist.add_before(2,Node(9))
# llist.remove_node(8)
# llist.remove_node(7)
print(len(llist))
# print(llist.get_ele(0))
print(llist)
llist.reverse()
print(llist)

    