import unittest

from classes.Graph import Graph


class GraphTest(unittest.TestCase):

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

    def test_graphs_vertexes(self):
        self.assertEqual([1, 3, 4, 5, 6, 2], list(self.firstGraph.connections.keys()))
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], list(self.secondGraph.connections.keys()))

    def test_graphs_connections(self):
        self.assertEqual(
            {1: [(3, 10)],
             3: [(1, 10), (4, 80), (2, 40)],
             4: [(3, 80), (5, 50), (2, 100)],
             5: [(4, 50), (6, 20)],
             6: [(5, 20)],
             2: [(3, 40), (4, 100)]
             },
            self.firstGraph.connections
        )

        self.assertEqual(
            {1: [(2, 20), (4, 20)],
             2: [(1, 20), (3, 20), (5, 10)],
             3: [(2, 20), (6, 20)],
             6: [(3, 20), (9, 20), (5, 10)],
             9: [(6, 20), (8, 20)],
             8: [(9, 20), (7, 20), (5, 10)],
             7: [(8, 20), (4, 20)],
             4: [(7, 20), (1, 20), (5, 10)],
             5: [(2, 10), (4, 10), (6, 10), (8, 10)]
             }, self.secondGraph.connections
        )

        self.assertEqual(
            {1: [(2, 50)],
             2: [(1, 50), (3, 1000000000)],
             3: [(2, 1000000000)]
             }, self.thirdGraph.connections
        )

    def test_graph_wrong_inputs(self):
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, '1', 2, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, '2', 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2, '3')
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1.5, 2, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2.5, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2, 3.5)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, {1}, 2, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, {2}, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2, {3})
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, [1], 2, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, [2], 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2, [3])
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, (1,), 2, 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, (2,), 3)
        self.assertRaises(TypeError, self.firstGraph.create_edges_from_vertexes, 1, 2, (3,))
        self.assertRaises(ValueError, self.firstGraph.create_edges_from_vertexes, 1, 2, -3)


if __name__ == '__main__':
    unittest.main()
