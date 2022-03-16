import numpy as np
from building import *

class Wall(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y)
    
    def add_wall(self, grid):
        
        x = self.get_x()
        y = self.get_y()

        grid[x][y] = '#' 

