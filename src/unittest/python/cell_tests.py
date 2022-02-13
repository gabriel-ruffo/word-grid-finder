import sys
import unittest

sys.path.append("C:/Users/gabri/OneDrive/Documents/PersonalProjects/word-grid-finder/src/main/python/")

from cell import Cell

class CellTests(unittest.TestCase):
    def test_make_cell_and_get_fields(self):
        cellTrue = Cell("a", True)
        cellDefault = Cell("b")

        self.assertTrue(cellTrue.get_visited())
        self.assertEqual("a", cellTrue.get_letter())

        self.assertFalse(cellDefault.get_visited())
        self.assertEqual("b", cellDefault.get_letter())

        cellDefault.set_visited(True)
        self.assertTrue(cellDefault.get_visited())


if __name__ == '__main__':
    unittest.main()