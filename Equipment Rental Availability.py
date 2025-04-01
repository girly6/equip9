from collections import deque

def shortest_path_to_equipment(n, edges, availability, start_provider, target_equipment):
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS initialization
    queue = deque([(start_provider, [start_provider])])  # (current node, path)
    visited = set()
    
    while queue:
        provider, path = queue.popleft()
        
        # Check if this provider has the required equipment
        if target_equipment in availability.get(provider, []):
            return path
        
        # Mark as visited
        visited.add(provider)
        
        # Explore neighbors
        for neighbor in graph[provider]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return -1  # If no provider has the requested equipment

# User Input
n = int(input("Enter number of rental providers: "))
m = int(input("Enter number of connections: "))

edges = []
for _ in range(m):
    u, v = map(int, input("Enter connection (providerA providerB): ").split())
    edges.append((u, v))

availability = {}
for i in range(1, n + 1):
    equipment = input(f"Enter available equipment for provider {i} (comma-separated, or leave empty): ")
    availability[i] = equipment.split(",") if equipment else []

start_provider = int(input("Enter the starting provider: "))
target_equipment = input("Enter the equipment type you're looking for: ")

# Output the result
result = shortest_path_to_equipment(n, edges, availability, start_provider, target_equipment)
if result == -1:
    print("No provider has the requested equipment.")
else:
    print("Shortest path to provider with requested equipment:", result)
