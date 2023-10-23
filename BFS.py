def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    front, rear = 0, 1

    while front < rear:
        current_node = queue[front]
        front += 1

        if current_node not in visited:
            visited.add(current_node)
            print(current_node) 

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    rear += 1

if __name__ == "__main__":
 
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'B', 'D', 'E'],
        'C': ['A','F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }

    start_node = 'A' 
    bfs(graph, start_node)
