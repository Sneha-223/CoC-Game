import numpy as np
from colorama import Fore, Back, Style

class Map:

    #Creates the entire board for the game

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols=cols
        self.grid=[]
        self.__flag=0
        self.color_grid = []
    
    #function to create the playing board
    def create_map(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                self.temp.append("-")
            self.grid.append(self.temp)
        
        for i in range(self.__rows):
            self.temp1=[]
            for j in range(self.__cols):
                self.temp1.append("w")
            self.color_grid.append(self.temp1)
        

    #printing the map
    def print_map(self):

            color = Fore.WHITE

            for i in range(self.__rows):
                for j in range (self.__cols):
                     
                    #print(Back.GREEN + self.grid[i][j],end='')
                    if self.color_grid[i][j] == 'w':
                        color = Fore.WHITE
                    if self.color_grid[i][j] == 'g':
                        color = Fore.GREEN
                    if self.color_grid[i][j] == 'y':
                        color = Fore.YELLOW
                    if self.color_grid[i][j] == 'r':
                        color = Fore.RED

                    print(color + self.grid[i][j] + Fore.RESET, end='')
                    #print(Fore.RESET)

                print()

            #print(Back.RESET)

            #print()

            
            
            #print(Fore.RESET)

    # #add town hall to the map
    # def add_town_hall(self):

    #     for i in range(self.__rows//2 - 2, self.__rows//2 + 2):
    #             for j in range(self.__cols//2 -2, self.__cols//2 +1):
    #                 self.grid[i][j] = "T"
    #                 #print(Fore.RED + self.grid[i][j], end='')
        
    # def add_huts(self, x, y, length, width):

    #     for i in range(x, x+length):
    #             for j in range(y, y+width):
    #                 self.grid[i][j] = "H"


