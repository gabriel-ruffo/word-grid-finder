import logging
import sys

from cell import Cell


class Grid:
    def __init__(self):
        self.__setup_logger()
        self.path_prefix = "src/main/files/"
        self.grid_array = []


    def __setup_logger(self):
        """Constructs logger with out stream to console"""
        self.logger = logging.getLogger("gridlogger")
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            handler = logging.StreamHandler(stream=sys.stdout)
            formatter = logging.Formatter("[%(levelname)s] %(name)s(%(lineno)s): %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def construct_grid_from_text_file(self, file_path):
        """Populates 2D list with items from given text file.

        Args:
            file_path (String): Path to file containing comma separated
                grid values
        """
        with open(self.path_prefix + file_path) as f:
            for line in f:
                # construct list from line of comma separated letters
                line = line.rstrip()
                line_list = line.split(",")
                cell_list = [Cell(str(letter)) for letter in line_list]
                self.grid_array.append(cell_list)
        self.logger.debug("Grid from file: " + str(self.grid_array))


    def get_rows_size(self):
        return len(self.grid_array)


    def get_cols_size(self):
        return len(self.grid_array[0])


    def get_cell(self, row, column):
        return self.grid_array[row][column]


    def set_cell(self, row, column, cell):
        self.grid_array[row][column] = cell
    

    def visit_cell(self, row, column, visit):
        self.grid_array[row][column].set_visited(visit)
        
        
    def get_cell_index(self, cell):
        for row, col in enumerate(self.grid_array):
            if cell in col:
                return (row, col.index(cell))
