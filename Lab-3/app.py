from modules.dejkstra_algorithm import dejkstra_algorithm
from modules.get_data import get_data
from modules.write_data import write_data


def main():
    n, m, clients, graph = get_data('in_files/first_in')
    min_max_latency = None
    for vertex_id in graph.connections:
        if vertex_id not in clients:
            current_latencies = dejkstra_algorithm(graph, vertex_id)
            current_max_latency = max([current_latencies[client] for client in clients])
            if min_max_latency is None:
                min_max_latency = current_max_latency
            elif current_max_latency < min_max_latency:
                min_max_latency = current_max_latency

    write_data('out_files/first_out', min_max_latency)

    return min_max_latency


if __name__ == '__main__':
    print(main())
