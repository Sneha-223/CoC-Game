import numpy as np
from building import *

class Cannon(Building):

    def __init__(self, x, y, length, width):
        Building.__init__(self, x, y, length, width)
    
    def add_cannon(self, grid):
        
        x = self.get_x()
        y = self.get_y()
        length = self.get_width()
        width = self.get_length()

        for i in range(x, x + length):
                for j in range(y, y + width):
                    grid[i][j] = 'C' 

        