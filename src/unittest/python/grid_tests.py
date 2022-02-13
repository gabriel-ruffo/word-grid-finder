import sys
import unittest

sys.path.append("C:/Users/gabri/OneDrive/Documents/PersonalProjects/word-grid-finder/src/main/python/")

from grid import Grid
from cell import Cell


class GridTest(unittest.TestCase):
    def test_create_grid_from_text_file(self):
        grid = Grid()
        grid.construct_grid_from_text_file("simple_grid.txt")
        cell_0_0 = grid.get_cell(0, 0)

        self.assertEqual("x", cell_0_0.get_letter())
        self.assertFalse(cell_0_0.get_visited())

        new_cell = Cell("y")
        grid.set_cell(0, 0, new_cell)

        self.assertEqual("y", grid.get_cell(0, 0).get_letter())
        self.assertFalse(grid.get_cell(0, 0).get_visited())

        grid.visit_cell(0, 0, True)
        self.assertTrue(grid.get_cell(0, 0).get_visited())

        self.assertEqual(3, grid.get_rows_size())
        self.assertEqual(3, grid.get_cols_size())
        
        
    def test_grid_indexing(self):
        grid = Grid()
        grid.construct_grid_from_text_file("simple_grid.txt")
        cell_0_0 = grid.get_cell(0, 0)
        cell_0_1 = grid.get_cell(0, 1)
        
        self.assertEqual("x", cell_0_0.get_letter())
        self.assertEqual("x", cell_0_1.get_letter())
    
        self.assertEqual((0, 0), grid.get_cell_index(cell_0_0))
        self.assertEqual((0, 1), grid.get_cell_index(cell_0_1))


if __name__ == '__main__':
    unittest.main()