from classes.Graph import Graph
from modules.dejkstra_algorithm import dejkstra_algorithm
import unittest


class DejkstraTest(unittest.TestCase):

    def setUp(self) -> None:
        self.firstGraph = Graph()

        self.firstGraph.create_edges_from_vertexes(1, 3, 10)
        self.firstGraph.create_edges_from_vertexes(3, 4, 80)
        self.firstGraph.create_edges_from_vertexes(4, 5, 50)
        self.firstGraph.create_edges_from_vertexes(5, 6, 20)
        self.firstGraph.create_edges_from_vertexes(2, 3, 40)
        self.firstGraph.create_edges_from_vertexes(2, 4, 100)

        self.secondGraph = Graph()

        self.secondGraph.create_edges_from_vertexes(1, 2, 20)
        self.secondGraph.create_edges_from_vertexes(2, 3, 20)
        self.secondGraph.create_edges_from_vertexes(3, 6, 20)
        self.secondGraph.create_edges_from_vertexes(6, 9, 20)
        self.secondGraph.create_edges_from_vertexes(9, 8, 20)
        self.secondGraph.create_edges_from_vertexes(8, 7, 20)
        self.secondGraph.create_edges_from_vertexes(7, 4, 20)
        self.secondGraph.create_edges_from_vertexes(4, 1, 20)
        self.secondGraph.create_edges_from_vertexes(5, 2, 10)
        self.secondGraph.create_edges_from_vertexes(5, 4, 10)
        self.secondGraph.create_edges_from_vertexes(5, 6, 10)
        self.secondGraph.create_edges_from_vertexes(5, 8, 10)

        self.thirdGraph = Graph()

        self.thirdGraph.create_edges_from_vertexes(1, 2, 50)
        self.thirdGraph.create_edges_from_vertexes(2, 3, 1000000000)

    def test_dejkstra(self):
        self.assertRaises(ValueError, dejkstra_algorithm, self.firstGraph, 0)
        self.assertEqual({1: 0, 3: 10, 4: 90, 5: 140, 6: 160, 2: 50},
                         dejkstra_algorithm(self.firstGraph, 1))
        self.assertEqual({1: 50, 3: 40, 4: 100, 5: 150, 6: 170, 2: 0},
                         dejkstra_algorithm(self.firstGraph, 2))
        self.assertEqual({1: 10, 3: 0, 4: 80, 5: 130, 6: 150, 2: 40},
                         dejkstra_algorithm(self.firstGraph, 3))
        self.assertEqual({1: 90, 3: 80, 4: 0, 5: 50, 6: 70, 2: 100},
                         dejkstra_algorithm(self.firstGraph, 4))
        self.assertEqual({1: 140, 3: 130, 4: 50, 5: 0, 6: 20, 2: 150},
                         dejkstra_algorithm(self.firstGraph, 5))
        self.assertEqual({1: 160, 3: 150, 4: 70, 5: 20, 6: 0, 2: 170},
                         dejkstra_algorithm(self.firstGraph, 6))


if __name__ == '__main__':
    unittest.main()
