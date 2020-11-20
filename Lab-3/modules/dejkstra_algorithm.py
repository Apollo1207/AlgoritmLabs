import sys
from queue import PriorityQueue

from classes.Graph import Graph


def dejkstra_algorithm(graph: Graph, start_vertex_id: int):
    distances = {vertex_id: sys.maxsize for vertex_id in graph.connections}
    distances[start_vertex_id] = 0

    if start_vertex_id not in graph.connections:
        raise ValueError('Not found start_vertex_id in_files graph vertexes')

    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_vertex_id))

    while not available_vertexes_queue.empty():
        parent_vertex = available_vertexes_queue.get()[1]

        for child_vertex_tuple in graph.connections[parent_vertex]:
            distance = distances[parent_vertex] + child_vertex_tuple[1]
            child_vertex_id = child_vertex_tuple[0]

            if distance < distances[child_vertex_id]:
                distances[child_vertex_id] = distance
                available_vertexes_queue.put((distance, child_vertex_id))

    return distances
