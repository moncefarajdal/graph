mono_graph = {
    "type": "Server",
    "id": '3ee14962-4760-4af0-bf95-78794d7797d9',
    "price": 10.3,
    "description": "Server used for mobile app",
    "connected_to" : []
 }

small_graph= {
    "type": "Server",
    "id": "3ee14962-4760-4af0-bf95-78794d7797d9",
    "price": 10.3,
    "description": "Server used for mobile app",
    "connected_to": [
        {
            "type": "LoadBalancer",
            "id": "5fa3c567-8bd4-4ea4-8d60-43827f35d32a",
            "price": "25.5",
            "connected_to": [
                {
                    "type": "Router",
                    "id": "7bc8e6d1-4f32-4768-a1f2-b6e0f9bb5c2a",
                    "price": 15.75,
                    "description": "Primary router for east region",
                    "connected_to": []
                },
                {
                    "type": "Router",
                    "id": "7bc8e6d1-4f32-4768-a1f2-b6e0f9bb5c2a",
                    "price": 15.75,
                    "description": "Primary router for east region",
                    "connected_to": []
                }
            ]
        },
        {
            "type": "Cluster",
            "id": "9de4f88a-6aa5-4a9b-8c25-b427f1c58c3d",
            "price": "45",
            "description": "Database cluster",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "3ee14962-4760-4af0-bf95-78794d7797d9",
                    "price": 10.3,
                    "description": "Server used for mobile app",
                    "connected_to": []
                }
            ]
        }
    ]
}


medium_graph = {
    "type": "LoadBalancer",
    "id": "1aa2b3c4-5d6e-7f89-0123-456789abcdef",
    "price": "150.99",
    "description": "Main entry point load balancer",
    "connected_to": [
        {
            "type": "Cluster",
            "id": "2bb3c4d5-6e7f-8901-2345-6789abcdef01",
            "price": 299.99,
            "description": "Web application cluster",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "3cc4d5e6-7f89-0123-4567-89abcdef0123",
                    "price": "45.50",
                    "description": "Primary web server",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4dd5e6f7-8901-2345-6789-abcdef012345",
                            "price": 75.25,
                            "connected_to": []
                        }
                    ]
                },
                {
                    "type": "Server",
                    "id": "3cc4d5e6-7f89-0123-4567-89abcdef0123",
                    "price": "45.50",
                    "description": "Primary web server",
                    "connected_to": []
                }
            ]
        },
        {
            "type": "Cluster",
            "id": "5ee6f7g8-9012-3456-7890-abcdef012345",
            "price": 275.00,
            "description": "Database cluster",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "6ff7g8h9-0123-4567-89ab-cdef01234567",
                    "price": "85.75",
                    "connected_to": [
                        {
                            "type": "Server",
                            "id": "3cc4d5e6-7f89-0123-4567-89abcdef0123",
                            "price": "45.50",
                            "description": "Primary web server",
                            "connected_to": []
                        }
                    ]
                },
                {
                    "type": "Server",
                    "id": "7gg8h9i0-1234-5678-90ab-cdef01234567",
                    "price": 82.25,
                    "description": "Secondary database server",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4dd5e6f7-8901-2345-6789-abcdef012345",
                            "price": 75.25,
                            "connected_to": []
                        }
                    ]
                }
            ]
        },
        {
            "type": "Ip",
            "id": "8hh9i0j1-2345-6789-0abc-def012345678",
            "price": "5.00",
            "description": "Public IP address",
            "connected_to": [
                {
                    "type": "Router",
                    "id": "4dd5e6f7-8901-2345-6789-abcdef012345",
                    "price": 75.25,
                    "connected_to": []
                }
            ]
        }
    ]
}

tree ={
    "type": "LoadBalancer",
    "id": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
    "price": "199.99",
    "description": "Primary load balancer",
    "connected_to": [
        {
            "type": "Cluster",
            "id": "2b3c4d5e-6f78-90ab-cdef-123456789012",
            "price": 250.00,
            "description": "Application cluster A",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "3c4d5e6f-7890-abcd-ef12-34567890abcd",
                    "price": "45.50",
                    "description": "App server 1",
                    "connected_to": [
                        {
                            "type": "Ip",
                            "id": "4d5e6f78-90ab-cdef-1234-567890abcdef",
                            "price": 5.25,
                            "connected_to": []
                        }
                    ]
                }
            ]
        },
        {
            "type": "Router",
            "id": "5e6f7890-abcd-ef12-3456-7890abcdef12",
            "price": "80.00",
            "description": "Edge router",
            "connected_to": [
                {
                    "type": "Ip",
                    "id": "6f7890ab-cdef-1234-5678-90abcdef1234",
                    "price": 5.25,
                    "connected_to": []
                },
                {
                    "type": "Ip",
                    "id": "6f7890ab-cdef-1234-5678-90abcdef1234",
                    "price": 5.25,
                    "connected_to": []
                }
            ]
        }
    ]
}

large_graph ={
    "type": "LoadBalancer",
    "id": "1a1a1a1a-1111-1111-1111-1a1a1a1a1a1a",
    "price": "299.99",
    "description": "Global load balancer",
    "connected_to": [
        {
            "type": "Cluster",
            "id": "2b2b2b2b-2222-2222-2222-2b2b2b2b2b2b",
            "price": 450.00,
            "description": "Web cluster - US East",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "3c3c3c3c-3333-3333-3333-3c3c3c3c3c3c",
                    "price": "85.50",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4d4d4d4d-4444-4444-4444-4d4d4d4d4d4d",
                            "price": 75.25,
                            "description": "Primary router",
                            "connected_to": [
                                {
                                    "type": "Server",
                                    "id": "3c3c3c3c-3333-3333-3333-3c3c3c3c3c3c",
                                    "price": "85.50",
                                    "connected_to": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "LoadBalancer",
                    "id": "5e5e5e5e-5555-5555-5555-5e5e5e5e5e5e",
                    "price": 199.99,
                    "description": "Internal load balancer",
                    "connected_to": [
                        {
                            "type": "Server",
                            "id": "3c3c3c3c-3333-3333-3333-3c3c3c3c3c3c",
                            "price": "85.50",
                            "connected_to": []
                        },
                        {
                            "type": "Server",
                            "id": "6f6f6f6f-6666-6666-6666-6f6f6f6f6f6f",
                            "price": 82.25,
                            "connected_to": [
                                {
                                    "type": "Router",
                                    "id": "4d4d4d4d-4444-4444-4444-4d4d4d4d4d4d",
                                    "price": 75.25,
                                    "description": "Primary router",
                                    "connected_to": []
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "type": "Cluster",
            "id": "7g7g7g7g-7777-7777-7777-7g7g7g7g7g7g",
            "price": "475.50",
            "description": "Database cluster",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "8h8h8h8h-8888-8888-8888-8h8h8h8h8h8h",
                    "price": 95.00,
                    "description": "Primary DB",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4d4d4d4d-4444-4444-4444-4d4d4d4d4d4d",
                            "price": 75.25,
                            "description": "Primary router",
                            "connected_to": []
                        },
                        {
                            "type": "Server",
                            "id": "9i9i9i9i-9999-9999-9999-9i9i9i9i9i9i",
                            "price": "92.50",
                            "description": "Backup DB",
                            "connected_to": [
                                {
                                    "type": "Ip",
                                    "id": "0j0j0j0j-0000-0000-0000-0j0j0j0j0j0j",
                                    "price": 5.00,
                                    "connected_to": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "Server",
                    "id": "9i9i9i9i-9999-9999-9999-9i9i9i9i9i9i",
                    "price": "92.50",
                    "description": "Backup DB",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4d4d4d4d-4444-4444-4444-4d4d4d4d4d4d",
                            "price": 75.25,
                            "description": "Primary router",
                            "connected_to": []
                        }
                    ]
                }
            ]
        },
        {
            "type": "Cluster",
            "id": "aaaa1111-2222-3333-4444-555555555555",
            "price": 425.00,
            "description": "Cache cluster",
            "connected_to": [
                {
                    "type": "Server",
                    "id": "bbbb2222-3333-4444-5555-666666666666",
                    "price": "65.00",
                    "description": "Cache server 1",
                    "connected_to": [
                        {
                            "type": "Router",
                            "id": "4d4d4d4d-4444-4444-4444-4d4d4d4d4d4d",
                            "price": 75.25,
                            "description": "Primary router",
                            "connected_to": []
                        }
                    ]
                }
            ]
        }
    ]
}

datasource = [small_graph, medium_graph, large_graph, tree]

def total_graph_items(start_node):
    to_visit = [start_node]
    visited = []
    total_price = 0.0

    while to_visit:
        if to_visit[0].get("id") not in visited:
            visited.append(to_visit[0].get("id"))
            total_price += float(to_visit[0].get("price"))

        for node in to_visit[0].get("connected_to"):
            to_visit.append(node)

        to_visit.pop(0)
    
    return len(visited), total_price

total_items, total_price = total_graph_items(small_graph)
print(f"Length of the graph is {total_items} & total price is {total_price}")
