import numpy as np

class Building:

    def __init__(self, x, y, length, width):
        self.__x = x
        self.__y = y
        self.__length = length 
        self.__width = width

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width

    def set_parameters(self, x, y, length, width):
        self.__x = x
        self.__y = y
        self.__length = length
        self.__width = width

    # def show_building(self):
    #     for i in range(x, x+length):
    #             for j in range(y, y+width):
    #                 grid[i][j] = "H"    

    
