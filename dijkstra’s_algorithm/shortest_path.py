example_graph1= {
    'A': {'B': 3, 'C': 5},
    'B': {'D': 6},
    'C': {'D': 1},
    'D': {},
}
example_graph2 = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

import heapq
def calcuate_distances(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    pq = [(0, start_vertex)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq); 
        if current_distance > distances[current_vertex]:
            continue
        for nearby_vertex, vertex_distance in graph[current_vertex].items():
            distance = current_distance + vertex_distance
            if distance < distances[nearby_vertex]:
                distances[nearby_vertex] = distance
                heapq.heappush(pq, (distance, nearby_vertex))
    return distances

print(calcuate_distances(example_graph1, 'A'))
print(calcuate_distances(example_graph2, 'X'))

