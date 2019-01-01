import unittest

import computor


class TestComputor(unittest.TestCase):

    def test_first_degree(self):
        self.assertEqual(computor.first_degree_solver(1, 1), -1)
        self.assertEqual(computor.first_degree_solver(2, -1), 0.5)
        self.assertEqual(computor.first_degree_solver(0, 0), 'Inf')
        self.assertIs(computor.first_degree_solver(0, 1), None)

    def test_second_degree(self):
        self.assertEqual(computor.second_degree_solver(1, 2, 1, False), (-1, None, None))
        self.assertEqual(computor.second_degree_solver(1, 2, 1, True), (-1, None, None))
        self.assertEqual(computor.second_degree_solver(1, 0, -0.25, False), (None, -0.5, 0.5))
        self.assertEqual(computor.second_degree_solver(1, 0, 1, False), (None, -1j, 1j))

    def test_equation_info(self):
        self.assertEqual(computor.equation_info([0, 0, 0, 0]), 0)
        self.assertEqual(computor.equation_info([1, 0, 0, 0]), 0)
        self.assertEqual(computor.equation_info([2, -3, 0, 0]), 1)
        self.assertEqual(computor.equation_info([-1, 0, 4, 0]), 2)
        self.assertEqual(computor.equation_info([-1, 0]), 0)
        self.assertEqual(computor.equation_info([-1, 0, 1, 2, 4, -5, 0, 7]), 7)
        self.assertEqual(computor.equation_info([-1, 0, 1, 2, 4, -5, 0, 0, 0, 0, 0, 0, 12]), 12)


if __name__ == "__main__":
    unittest.main()
