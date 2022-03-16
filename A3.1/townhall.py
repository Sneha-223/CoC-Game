from email.base64mime import header_length
from matplotlib.pyplot import grid
import numpy as np
from building import *
from colorama import Fore, Back, Style
from global_vars import *

class Townhall(Building):

    def __init__(self, x, y, length, width):

        self.health = 100
        self.__color = Fore.GREEN

        Building.__init__(self, x, y, length, width)
    
    def add_townhall(self, grid):
        
        x = self.get_x()
        y = self.get_y()
        length = self.get_width()
        width = self.get_length()

        for i in range(x, x + length):
                for j in range(y, y + width):
                    grid[i][j] = 'T' 

    # def show_townhall(self, grid):
        
    #     x = self.get_x()
    #     y = self.get_y()
    #     length = self.get_width()
    #     width = self.get_length()

    #     for i in range(x, x + length):
    #         for j in range(y, y + width):
    #             grid[i][j] = self.__color + 'T' + Fore.RESET
                
    def set_color(self, color_grid, grid):
        
        x = self.get_x()
        y = self.get_y()
        length = self.get_width()
        width = self.get_length()
        #self.__health = health

        color_char = 'w'

        if self.health <= 100 and self.health >= 61:
            self.__color = Fore.GREEN
            color_char = 'g'

        if self.health <= 60 and self.health >= 9:
            self.__color = Fore.YELLOW
            color_char = 'y'

        if self.health <= 10 and self.health >= 1:
            self.__color = Fore.RED
            color_char = 'r'

        for i in range(x, x + length):
            for j in range(y, y + width):
                # if grid[i][j] == 'T':
                color_grid[i][j] = color_char

                if self.health <= 0 and grid[i][j] == 'T':
                    grid[i][j] = '-'
                    
        
    def set_health(self, health):
        self.health = health