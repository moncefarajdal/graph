from models import Graph, Node

graph = Graph()

server = Node("3ee14962-4760-4af0-bf95-78794d7797d9", "Server", price=10.3, description="Server used for mobile app")
load_balancer = Node("5fa3c567-8bd4-4ea4-8d60-43827f35d32a", "LoadBalancer", price=25.5, description="")
router = Node("7bc8e6d1-4f32-4768-a1f2-b6e0f9bb5c2a", "Router", price=15.75, description="Primary router for east region")
cluster = Node("9de4f88a-6aa5-4a9b-8c25-b427f1c58c3d", "Cluster", price=45.0, description="Database cluster")

graph.add_node(server)
graph.add_node(load_balancer)
graph.add_node(router)
graph.add_node(cluster)

graph.add_edge("3ee14962-4760-4af0-bf95-78794d7797d9", "5fa3c567-8bd4-4ea4-8d60-43827f35d32a")  # Server to LoadBalancer
graph.add_edge("5fa3c567-8bd4-4ea4-8d60-43827f35d32a", "7bc8e6d1-4f32-4768-a1f2-b6e0f9bb5c2a")  # LoadBalancer to Router
graph.add_edge("9de4f88a-6aa5-4a9b-8c25-b427f1c58c3d", "3ee14962-4760-4af0-bf95-78794d7797d9")  # Cluster to Server

def is_tree(graph):
    if len(graph.nodes) == 0:
        return False

    visited = set()

    def dfs(root):
        visited.add(root.id)
        for edge in root.edges:
            neighbor = edge.end_node
            if neighbor.id not in visited:
                if not dfs(neighbor):
                    return False
        return True

    start_node = list(graph.nodes.values())[0]
    if not dfs(start_node):
        return False

    return len(visited) == len(graph.nodes)


total_price = 0.0
for node in graph.nodes.values():
    total_price += node.price if node.price is not None else 0

print(f"Total nodes in the graph: {len(graph.nodes)}")
print(f"Total price of the graph: {total_price}")
print(f"Is the graph a tree? {'Yes' if is_tree(graph) else 'No'}")
