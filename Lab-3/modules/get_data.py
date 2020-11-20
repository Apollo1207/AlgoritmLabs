from classes.Graph import Graph


def get_data(filename: str):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
        n, m = tuple(int(x) for x in lines[0].split())
        clients = tuple(int(x) for x in lines[1].split())
        for line in lines[2:]:
            start, end, weight = tuple(int(x) for x in line.split())
            graph.create_edges_from_vertexes(start, end, weight)

    return n, m, clients, graph
