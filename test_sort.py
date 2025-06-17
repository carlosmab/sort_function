import unittest
from sort import sort

class TestPackageSorter(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_bulky_only(self):
        self.assertEqual(sort(160, 20, 20, 10), "SPECIAL")

    def test_heavy_only(self):
        self.assertEqual(sort(20, 20, 20, 25), "SPECIAL")

    def test_both_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 30), "REJECTED")

    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # volume == 1_000_000

    def test_edge_case_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")  # max(width, height, length) == 150

    def test_edge_case_mass(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")  # mass == 20

if __name__ == '__main__':
    unittest.main()