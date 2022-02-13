import logging
import sys

from grid import Grid
from dictionary_checker import DictionaryChecker


class WordFinder:
    def __init__(self, filename):
        self.__setup_logger()
        self.grid = Grid()
        self.grid.construct_grid_from_text_file(filename)
        self.dictionary = DictionaryChecker()
        self.global_found_words = []


    def __setup_logger(self):
        self.logger = logging.getLogger("finderlogger")
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            handler = logging.StreamHandler(stream=sys.stdout)
            formatter = logging.Formatter("[%(levelname)s] %(name)s(%(lineno)s): %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)


    def generate_word_list(self):
        """Starting with a source cell, go through all valid neighboring
        paths to find completed words.

        Returns:
            List: list of found completed words
        """
        rows = self.grid.get_rows_size()
        cols = self.grid.get_cols_size()
        
        for row in range(rows):
            for col in range(cols):
                # grab source cell
                current_cell = self.grid.get_cell(row, col)
                if not current_cell.get_letter():
                    continue
                # append all found valid words to found_words
                self.__generate_possible_words(current_cell)
        return self.global_found_words
                
                
    def __generate_possible_words(self, current_cell, running_string = ""):
        """Starting from a source cell (may not be source cell from generate_word_list),
        grab all valid neighboring cells, and pass to __follow_letter_path to build a
        word string to potentially find full valid words.

        Args:
            current_cell (Cell): Source cell from which to generate neighbors
            running_string (str, optional): Running string building to a full word. Defaults to "".

        Returns:
            String: Completed words or empty 
        """
        current_cell.set_visited(True)
        starting_row, starting_col = self.grid.get_cell_index(current_cell)
        searchable_cells = self.__get_valid_neighbor_cells(starting_row, starting_col)
        if searchable_cells:
            self.__check_running_string_in_dictionary(running_string)
            self.__follow_letter_path(current_cell, searchable_cells, running_string)
        else:
            # at this point, there are no more valid neighbor cells, can check for completed word
            self.__check_running_string_in_dictionary(running_string)
        current_cell.set_visited(False)
        
    
    def __follow_letter_path(self, current_cell, searchable_cells, running_string):
        """For each cell in the list of valid neighbor cells, construct a running string.
        If that string is the a full/prefix word, then add it to a list of possible words.
        Then, for each possible word, recursively call __generate_possible_words with the
        running string and last accessed neighbor cell.

        Args:
            current_cell (Cell): Cell currently being observed and added to running_string
            searchable_cells (Cell): Valid neighbor cells from which to construct running_string
            running_string (String): Live string that could be a full/prefix word
        """
        possible_words = []
        for cell in searchable_cells:
            if not running_string:
                temp_string = current_cell.get_letter() + cell.get_letter()
            else:
                temp_string = running_string + cell.get_letter()
            if self.dictionary.check_if_word_starts_with_letters(temp_string):
                possible_words.append((temp_string, cell))
        for temp_string, last_cell in possible_words:
            self.__generate_possible_words(last_cell, temp_string)
    
        
    def __get_valid_neighbor_cells(self, starting_row, starting_col):
        searchable_cells = []
        neighbor_cells = [
            (starting_row - 1, starting_col - 1),   # up & left
            (starting_row - 1, starting_col),       # up
            (starting_row - 1, starting_col + 1),   # up & right
            (starting_row, starting_col - 1),       # left
            (starting_row, starting_col + 1),       # right
            (starting_row + 1, starting_col - 1),   # down & left
            (starting_row + 1, starting_col),       # down
            (starting_row + 1, starting_col + 1)    # down & right
        ]
        for row, col in neighbor_cells:
            if self.__is_not_within_limits(row, col):
                continue
            elif self.__cell_is_visited(row, col):
                continue
            elif self.__cell_is_empty(row, col):
                continue
            else:
                searchable_cells.append(self.grid.get_cell(row, col))
        return searchable_cells


    def __is_not_within_limits(self, row, col):
        return row < 0 or col < 0 or row >= self.grid.get_rows_size() or col >= self.grid.get_cols_size()


    def __cell_is_visited(self, row, col):
        return self.grid.get_cell(row, col).get_visited()
    
    
    def __cell_is_empty(self, row, col):
        return not self.grid.get_cell(row, col).get_letter()
        
        
    def __check_running_string_in_dictionary(self, running_string):
        if self.dictionary.check_word_in_dictionary(running_string) and len(running_string) >= 3:
                self.logger.debug("Found a word: {}".format(running_string))
                self.global_found_words.append(running_string)

