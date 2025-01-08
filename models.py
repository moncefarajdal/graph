class Node:
    def __init__(self, id:str, type:str, price: float = None, description: str = None):
        self.id = id
        self.type = type
        self.price = price
        self.description = description
        self.edges = []

    def add_edge(self, end_node):
        edge = Edge(self, end_node)
        self.edges.append(edge)

    def __repr__(self):
        return f"Node({self.id}, {self.type})"

 
class Edge:
    def __init__(self, start_node: Node, end_node: Node):
        self.start_node = start_node
        self.end_node = end_node

    def __repr__(self):
        return f"Edge({self.start_node.id} -> {self.end_node.id})"


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.id] = node

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def add_edge(self, start_node_id, end_node_id):
        start_node = self.get_node(start_node_id)
        end_node = self.get_node(end_node_id)
        if start_node and end_node:
            start_node.add_edge(end_node)

    def __repr__(self):
        return f"{self.nodes}"
